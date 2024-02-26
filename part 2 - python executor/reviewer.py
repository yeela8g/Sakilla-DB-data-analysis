import os
import mysql.connector
from dotenv import load_dotenv  # Load dotenv file
load_dotenv()  # Read the password from the environment variable

cnx = mysql.connector.connect(  # Create a connection
    user='root',
    password=os.getenv('MYSQL_ROOT_PASSWORD'),
    host='127.0.0.1',
    database='sakila'
)

cursor = cnx.cursor()  # Create a cursor
cnx.autocommit = True

cursor.execute("select * from information_schema.tables where table_schema = 'sakila' and table_name = 'reviewer';")
exist_reviewer = cursor.fetchall()
if not exist_reviewer:
    # Create the reviewer table
    cursor.execute("""
        CREATE TABLE reviewer (
          reviewer_id int NOT NULL PRIMARY KEY,
          first_name varchar(45) NOT NULL ,
          last_name varchar(45) NOT NULL 
        );
    """)

cursor.execute("select * from information_schema.tables where table_schema = 'sakila' and table_name = 'rating';")
exist_rating = cursor.fetchall()
if not exist_rating:
    # Create the rating table
    cursor.execute("""
        CREATE TABLE rating (
          film_id smallint UNSIGNED NOT NULL ,
          reviewer_id int NOT NULL,
          rating decimal(2,1) check ( rating >= 0 and rating < 10 ) NOT NULL ,
          primary key (film_id,reviewer_id),
          FOREIGN KEY (film_id) REFERENCES film(film_id) on delete cascade on update cascade ,
          FOREIGN KEY (reviewer_id) REFERENCES reviewer(reviewer_id) on delete cascade on update cascade
        );
    """)

ID = input("please enter ID: ")  #start interaction with clients:
query = "select * from sakila.reviewer where reviewer_id =%s"
cursor.execute(query, [ID])
result = cursor.fetchall()

if not result : # user id does not exist in the reviewer list - save this reviewer details
    first_name = input("please enter first name: ")
    last_name = input("please enter last name: ")
    query = "insert into reviewer() VALUES (%s,%s,%s);"
    values = [ID, first_name, last_name]
    cursor.execute(query,values)

query = "select * from sakila.reviewer where reviewer_id =%s"  # pull the reviewer from the table and say hello to him
cursor.execute(query, [ID])
result = cursor.fetchall()
print("hello, " + str(result[0][1] + " " + str(result[0][2])))

res = []
flag = 1
while flag:
    cursor.reset()
    film_name = input("please insert film name to rate:")
    query1 = "select * from sakila.film where title =%s"
    cursor.execute(query1, [film_name])
    result_temp = cursor.fetchall()
    res = result_temp
    if len(res):  #if name was founded at least once
        flag = 0
    else:  # if film name wasn't found in DB
        print("name not found, try again")
    if len(res) > 1:  # present all ID films and release year - of this name film.
        query2 = "select film_id, release_year from sakila.film where title =%s"
        cursor.execute(query2,[film_name])
        all_movies_conflicted = cursor.fetchone()
        while all_movies_conflicted:
            print(all_movies_conflicted)
            all_movies_conflicted = cursor.fetchone()
        request_filmID = input("choose film_id from the list: ")  # ask the user to choose specific film by its ID
        query3 = "select * from sakila.film where film_id = %s"
        cursor.execute(query3,[request_filmID])
        chosen_id_movie =cursor.fetchall()
        if not chosen_id_movie:
            print("id_movie not in the list, try again")
            flag = 1
        else:
            res = chosen_id_movie
            flag=0
rating = ""
invalid = 1
while invalid:
    rating_of_reviewer = input("please enter a rating:")
    try:
        if float(rating_of_reviewer) < 10 and float(rating_of_reviewer) >= 0  :  #if input is valid
            invalid = 0
            rating = rating_of_reviewer
    except:
        print("wrong input")
query4 = "select * from sakila.rating where film_id = %s and reviewer_id = %s"
query4_filmID = res[0][0]
cursor.execute(query4,[query4_filmID,ID])
existing_rating = cursor.fetchall()
if not existing_rating:
    query5 = "insert into rating() VALUES (%s,%s,%s);"
    values = [query4_filmID,ID, rating]
    cursor.execute(query5, values)
else:
    query6 = "UPDATE sakila.rating set rating.rating = %s where rating.film_id = %s and rating.reviewer_id = %s ;"
    values_for_update = [rating,query4_filmID,ID]
    cursor.execute(query6, values_for_update)
#printing query
cursor.execute('''
                select film.title,concat(reviewer.first_name, " ", reviewer.last_name),rating.rating 
                from film, rating, reviewer
                where film.film_id = rating.film_id and rating.reviewer_id = reviewer.reviewer_id;
               ''')
rating_line =cursor.fetchone()
while rating_line:
    print(rating_line)
    rating_line = cursor.fetchone()
cnx.close()  # Close the connection


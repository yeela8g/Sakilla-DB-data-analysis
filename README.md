# Sakilla-DB-data-analysis

## About the Sakila DB:
The Sakila database is a commonly used sample database designed for learning and practicing with SQL. It represents a fictional DVD rental store and contains various tables such as films, actors, customers, rentals, etc. Each table simulates real-world entities and their relationships. The structure of the database allows users to explore and understand SQL concepts like querying, joining tables, data manipulation, and more.

![image](https://github.com/yeela8g/Sakilla-DB-data-analysis/assets/118124478/fe0bf7c0-94de-4347-899d-299dd8fa403e)
------------------
This repositroy divided to two different parts.

## part 1 - SQL Queries
This part comprises different SQL queries aimed at answering specific data questions within the Sakila database. Each query is designed to retrieve precise information and is accompanied by documentation, including any assumptions made during query formulation. Queries are intended to be well-structured and executable in MySQL.
The SQL queries provided in this repository exemplify various foundational principles and practical skills in SQL programming. Below are the key theoretical concepts and applied knowledge demonstrated through the implementation of these queries:

- **Data Retrieval and Filtering**:
    These queries showcase the ability to extract specific data from database tables by applying filtering techniques such as WHERE clauses to refine the result set.
- **Joining Tables**:
  By combining multiple tables, these queries illustrate an understanding of relational database concepts and the ability to establish meaningful relationships between different entities   in the database.
- **Aggregation and Grouping**:
  Utilizing aggregation functions like COUNT(), SUM(), and AVG(), these queries compute summary statistics, demonstrating proficiency in summarizing data. GROUP BY clauses are employed     to group data based on certain attributes before applying these aggregate functions.
- **Subqueries and Nested Queries**:
  These queries employ subqueries and nested queries to execute complex operations. Subqueries are used to obtain intermediate results necessary for the main query, showcasing an ability   to tackle multifaceted data retrieval tasks.
- **Pattern Matching with Regular Expressions**:
    Regular expressions (REGEXP_LIKE) are utilized to perform pattern matching operations, enabling precise searches based on specific patterns or formats within text fields.
- **Set Operations (UNION)**:
  The use of the UNION operator merges the results of multiple SELECT statements into a single result set, facilitating the combination of data from different queries while ensuring        duplicate rows are eliminated.
- **Data Modification and Constraints**:
  Although not explicitly demonstrated, SQL principles related to data modification (INSERT, UPDATE, DELETE) and constraint management (PRIMARY KEY, FOREIGN KEY, CHECK constraints) are     fundamental aspects of SQL programming.
- **Optimization and Performance Considerations:**
  These queries are crafted with performance optimization in mind, considering factors such as indexing strategies, query execution plans, and minimizing unnecessary data retrieval to
  enhance efficiency.
-** Data Integrity and Referential Constraints:**
  The queries may rely on referential integrity constraints defined in the database schema to maintain data consistency and integrity across related tables, reflecting a commitment to      data quality and reliability.
- **error Handling and Debugging:**
  Understanding how to troubleshoot and debug SQL queries is emphasized, encompassing tasks such as identifying syntax errors, addressing logical inconsistencies, and implementing error-   handling mechanisms.

## part 2 - rating system
Python program for movie rating system that allows reviewers to rate films in a database.
It interacts with a MySQL database named "sakila" which contains tables for films, reviewers, and ratings. The program prompts users to enter their ID, first name, and last name if they are new reviewers, then allows them to rate movies by providing the film's name and their rating. If a film with the provided name is not found, the program prompts the user to try again. Additionally, if multiple films with the same name exist, the program displays a list of film IDs and release years for the user to choose from.

### How to Run:
  1. Ensure you have Python installed on your system.
  2. Install the required packages by running:
    ``` pip install mysql-connector-python python-dotenv ```
  3. Create a .env file in the project directory and add the following line, replacing YOUR_MYSQL_ROOT_PASSWORD with your actual MySQL         root password:
     ``` MYSQL_ROOT_PASSWORD=YOUR_MYSQL_ROOT_PASSWORD ```
  4. Ensure you have a MySQL server running with the Sakila sample database installed.
### Operations Available:
+ Add new reviewers to the database.
+ Rate movies by providing the movie name and rating.
+ Update existing ratings for movies.

### Usage:
Run the Python script movie_rating_system.py.
Upon execution, the program will prompt you to enter your ID.
![image](https://github.com/yeela8g/Sakilla-DB-data-analysis/assets/118124478/28a890eb-1c8a-457e-9361-40312515282c)

If you are a new reviewer, you will be asked to enter your first name and last name.
![image](https://github.com/yeela8g/Sakilla-DB-data-analysis/assets/118124478/eaa1573f-3468-405a-9e21-ef8b45ca26c5)

After entering your information, you can input the name of the movie you want to rate.
If the movie name is found in the database, you will be prompted to enter your rating for the movie.
The program will update the rating for the movie in the database if it already exists, otherwise, it will insert a new rating record.
Finally, the program will display all the movie ratings stored in the database.

![image](https://github.com/yeela8g/Sakilla-DB-data-analysis/assets/118124478/a684944c-1e7c-41eb-9451-148ae1a096fb)

### Referential Integrity Principle Implemented:

The program ensures referential integrity by implementing foreign key constraints in the database tables. Specifically, the rating table has foreign key constraints referencing the film and reviewer tables with ON DELETE CASCADE and ON UPDATE CASCADE options, ensuring that if a film or reviewer is deleted or updated, the corresponding ratings are also updated or deleted accordingly to maintain data consistency.

### Additinal information
+ This program assumes the existence of a MySQL server with the Sakila sample database installed. Make sure your MySQL server is running and accessible.
+ The .env file is used to securely store sensitive information like the MySQL root password. Ensure you keep this file secure and do not share it publicly.
+ The program uses input validation to ensure that only valid ratings (between 0 and 10) are accepted from users.

**enjoy!**

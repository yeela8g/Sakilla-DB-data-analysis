# Find all the actors who have acted in at least 10 movies more than the average number of movies per actor. 
# Return the first and last names of these actors, ordered by their first names and then by their last names.

select a.first_name  ,a.last_name
from actor as a, film_actor as fc
where a.actor_id = fc.actor_id
group by a.actor_id
having count(*) >= 10+(
						select avg(y.number_of_movies)
						from (
						SELECT actor_id ,count(film_id) as number_of_movies
						FROM film_actor
						group by actor_id) y)
order by a.first_name , a.last_name;

# the wuery was built with three nested queries , the two inner query returns the average number of films per actor. 
# the outter gives all the actors who acted in atleast 10 movies more. 
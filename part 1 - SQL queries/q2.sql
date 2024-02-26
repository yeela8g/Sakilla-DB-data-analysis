# Find all children-friendly films (i.e, less than 1.5 hours long and rated PG or G). Return film_id, and title.
SELECT distinct film_id, title
FROM sakila.film
WHERE length < 90
AND (rating ='PG' OR rating='G');

# List the average movie length for every film category.

SELECT c.name ,AVG(f.length) as avg_length
FROM film AS f ,film_category as fc , category AS c
where f.film_id = fc.film_id
AND fc.category_id = c.category_id
group by c.name;
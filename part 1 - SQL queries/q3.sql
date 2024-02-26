SELECT f.film_id,f.title as film_title, ft.title as film_text_title
FROM film AS f, film_text AS ft
WHERE f.film_id = ft.film_id 
AND f.title <> ft.title
order by f.title
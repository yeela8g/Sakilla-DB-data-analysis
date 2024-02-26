# How many weeks was the longest film rental? Who is the customer? What film did this customer rent?
# Return the customer’s full name (in one column), the film title and the rental duration in weeks (rounded to the first 4 decimal points).

SELECT concat(c.first_name," ",c.last_name) as full_name , f.title, datediff(return_date,rental_date)/7 as max_rental
FROM rental as r, inventory as i, film as f, customer as c
where r.customer_id = c.customer_id
and r.inventory_id = i.inventory_id
and i.film_id = f.film_id
and  (return_date - rental_date) = (select max(return_date - rental_date)
									from rental);

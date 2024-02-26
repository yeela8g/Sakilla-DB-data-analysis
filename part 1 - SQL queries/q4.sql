# Which customer rented the largest number of films in May 2005? 
# Return the customer’s full name in a single column.

select y.full_name
from (
SELECT CONCAT(c.first_name," ",c.last_name) as full_name , count(r.rental_id) as count_rent
FROM customer AS c , rental AS r
WHERE c.customer_id=r.customer_id
AND r.rental_date BETWEEN '2005-05-01' AND '2005-05-31'
group by full_name
ORDER BY count_rent DESC) y
LIMIT 1;

# It is a nested query. inner query returns customer full name and count of rents in requerd date. the table sorted by rental count. 
# the outter takes the first customer with the largest rental.
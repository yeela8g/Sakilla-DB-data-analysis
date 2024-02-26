# Find all customers and actors that do not have an actor or customer respectively with the same first name
# (Assume there are no actors who are also customers).

(SELECT c.first_name 
FROM customer c , actor a
where c.first_name <> a.first_name)
union
(SELECT a.first_name 
FROM customer c , actor a
where c.first_name <> a.first_name)

# assuming there are no actors who are also customers ,
and also the presenting of the actors and the customars by their name and not id.

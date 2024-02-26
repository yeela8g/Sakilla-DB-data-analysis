# Find all category names that contain the letter ‘a’ only once.
SELECT name
FROM category
#beggining,(everything that isn't a)* , than a , (everything that isn't a)* , end. 
WHERE REGEXP_LIKE(name,'^[^a]*a[^a]*$');

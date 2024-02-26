# Assume that we added a constraint with the script:
	#ALTER TABLE film
	#ADD CHECK (length>=10);
#Now we would like to delete it. To do so we need to run the following script:
	#ALTER TABLE film
	#DROP CONSTRAINT constraint_name;
#But we are missing the constraint name. What query can we run to get the film table constraint’s names?

select CONSTRAINT_NAME
from information_schema.TABLE_CONSTRAINTS
where TABLE_SCHEMA = 'sakila'
and TABLE_NAME = 'film';
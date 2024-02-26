# Return the store id, and the total “earning difference” of the store who had the largest difference in earning,
# between two succeeding months.

select max(t1.amount_sum-t2.amount_sum) as earning_diff,t1.store_id
from (
		SELECT sum(p.amount) as amount_sum,DATE_FORMAT(p.payment_date,'%Y.%m') as date_  ,c.store_id
		FROM  customer c, payment p 
		where c.customer_id = p.customer_id
		group by date_ , c.store_id) t1 
	join (
		SELECT sum(p.amount) as amount_sum,DATE_FORMAT(p.payment_date,'%Y.%m') as date_  ,c.store_id
		FROM  customer c, payment p 
		where c.customer_id = p.customer_id
		group by date_ , c.store_id) t2 
	on t1.store_id = t2.store_id 
where t1.date_ != t2.date_
and abs(t1.date_ -t2.date_)*120 < 2
group by t1.store_id
order by  earning_diff DESC
limit 1


# in the inner query created a duplicated table of monthly earning per store.
# the duplicating enabled to filter earning from two succeeding months, 
#and then in the outer the max earning diffrence was chosen.
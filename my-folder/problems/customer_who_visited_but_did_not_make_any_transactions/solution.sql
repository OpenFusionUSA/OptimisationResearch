# Write your MySQL query statement below
select V.customer_id , COUNT(*) as count_no_trans
from Visits V 
left join Transactions T
ON V.visit_id=T.visit_id 
where T.transaction_id is Null
group by V.customer_id;
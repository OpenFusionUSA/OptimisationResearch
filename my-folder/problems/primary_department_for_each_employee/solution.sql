# Write your MySQL query statement below


select employee_id,department_id
from employee
where employee_id in 
(
    select employee_id 
    from employee
    group by employee_id
    having count(distinct department_id)=1
) or primary_flag='Y';
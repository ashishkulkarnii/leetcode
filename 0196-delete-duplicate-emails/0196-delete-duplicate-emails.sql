# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete t1
from person as t1
inner join person as t2
where t1.id > t2.id and
    t1.email = t2.email
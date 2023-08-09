select product_name, sum(unit) as unit
from Orders as o
join Products as p
on o.product_id = p.product_id
where monthname(order_date) = "February" and year(order_date) = 2020
group by o.product_id
having sum(unit) >= 100;
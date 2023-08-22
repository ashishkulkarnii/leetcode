select distinct customer_id
from (
  select distinct *
  from Customer
) as c
right join Product as p
on c.product_key = p.product_key
group by customer_id
having count(p.product_key) = (
  select count(*)
  from Product
);
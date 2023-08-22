select s.product_id, s.year as first_year, s.quantity, s.price
from Sales as s
right join (
  select product_id, min(year) as year
  from Sales
  group by product_id
) as m
on s.product_id = m.product_id and s.year = m.year;
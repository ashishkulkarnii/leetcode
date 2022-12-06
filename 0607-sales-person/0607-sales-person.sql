select name
from salesperson
where name not in (
    select salesperson.name
    from salesperson, company, orders
    where salesperson.sales_id = orders.sales_id and
        company.com_id = orders.com_id and
        company.name = "RED"
)
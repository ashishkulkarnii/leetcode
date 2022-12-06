select customer_number
from orders
group by customer_number
having 
    count(customer_number)=(
        select count(*)
        from orders
        group by customer_number
        order by count(*) desc
        limit 1
    )


select user_id as buyer_id,
    join_date,
    count(order_id) as orders_in_2019
from orders
right join users
on users.user_id = orders.buyer_id and
    year(order_date) = 2019
group by user_id
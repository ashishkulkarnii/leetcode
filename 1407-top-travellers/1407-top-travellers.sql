select name,
    (
        case 
            when sum(distance) is null then 0
            else sum(distance)
        end
    ) as travelled_distance
from users
left join rides
on users.id = rides.user_id
group by user_id
order by travelled_distance desc,
    name asc
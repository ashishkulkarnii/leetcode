select activity_date as day,
    count(distinct user_id) as active_users
from activity
where datediff('2019-07-27', activity_date) <= 29 and
    datediff('2019-07-27', activity_date) >= 0
group by activity_date
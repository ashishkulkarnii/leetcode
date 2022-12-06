select t1.id
from weather as t1
inner join weather as t2
where date_sub(t1.recordDate, interval 1 day) = t2.recordDate and
    t1.temperature > t2.temperature
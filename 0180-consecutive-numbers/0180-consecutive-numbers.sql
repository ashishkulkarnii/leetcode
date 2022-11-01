select distinct t1.num as ConsecutiveNums
from Logs as t1,
    Logs as t2,
    Logs as t3
where t1.num = t2.num and t1.num = t3.num and
    t1.id = t2.id + 1 and t1.id = t3.id + 2
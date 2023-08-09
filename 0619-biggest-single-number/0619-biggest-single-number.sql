select ifnull(
  (
    select distinct num
    from MyNumbers
    group by num
    having count(num) = 1
    order by num desc
    limit 1
  ), null
) as num;
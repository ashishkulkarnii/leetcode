select machine_id, round(avg(processing_time), 3) as processing_time
from (
  select machine_id, t1.end - start as processing_time
  from (
    select machine_id, process_id, min(timestamp) as start, max(timestamp) as end
    from Activity
    group by machine_id, process_id
  ) as t1
  group by machine_id, process_id
) as t2
group by machine_id;
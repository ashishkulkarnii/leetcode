select user_id,
    CONCAT(UCASE(LEFT(name, 1)), LCASE(SUBSTRING(name, 2))) as name
from users
order by user_id
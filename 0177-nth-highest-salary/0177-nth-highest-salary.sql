CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        select salary
        from (
            select salary,
                dense_rank() over (order by salary desc) as myrank
            from employee
        ) as t
        where myrank = N
        order by salary desc
        limit 1
    );
END
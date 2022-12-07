(
    select employees.employee_id
    from employees, salaries
    where employees.employee_id not in (
        select employee_id
        from salaries
    )
)
union
(
    select salaries.employee_id
    from employees, salaries
    where salaries.employee_id not in (
        select employee_id
        from employees
    )
)
order by employee_id asc
select department.name as Department, e.name as Employee, e.salary as Salary
from employee as e, department
where 
    e.salary >= all (select salary from employee where employee.departmentid = e.departmentid)
    and e.departmentid = department.id
select unique_id, name
from Employees as e
left join EmployeeUNI as euni
on e.id = euni.id;
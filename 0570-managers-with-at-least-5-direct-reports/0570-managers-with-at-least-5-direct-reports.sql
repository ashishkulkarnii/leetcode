select e2.name
from Employee as e1, Employee as e2
where e1.managerId = e2.id
group by e1.managerId
having count(e1.managerId) >= 5;
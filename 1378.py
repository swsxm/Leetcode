SELECT  e2.unique_id, e1.id FROM Employees
RIGHT JOIN EmployeeUNI as e2 on e2.id = e1.id

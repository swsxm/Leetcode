SELECT e.name, b.bonus FROM Employee e
LEFT JOIN Bonus b on b.empId =  e.empId
WHERE b.bonus < 1000 or b.bonus is NULL;

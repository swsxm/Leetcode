DELETE p1
FROM Person AS p1
INNER JOIN Person AS p2
  ON p1.email = p2.email
WHERE p1.id > p2.id;


DELETE FROM Person WHERE id NOT IN (
    SELECT id FROM (
        SELECT min(id) as id from Person GROUP BY email
    ) as tmp
); 

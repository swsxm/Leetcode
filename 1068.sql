SELECT p.product_name, s.year, s.price FROM Sales s
INNER JOIN Product p on p.product_id = s.product_id

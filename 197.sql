SELECT t.id AS Id
FROM Weather t
INNER JOIN Weather f ON t.recordDate = DATE_ADD(f.recordDate, INTERVAL 1 DAY)
WHERE t.temperature > f.temperature;

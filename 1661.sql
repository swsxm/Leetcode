SELECT t1.machine_id, ROUND(AVG(t2.timestamp - t1.timestamp), 3) as processing_time FROM ACTIVITY t1
INNER JOIN  Activity t2 on t1.machine_id = t2.machine_id AND t1.process_id = t2.process_id
WHERE t1.activity_type = "start" AND t2.activity_type = "end"
GROUP BY t1.machine_id;


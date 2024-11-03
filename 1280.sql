SELECT s.student_id, 
       s.student_name, 
       subj.subject_name, 
       COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects subj
LEFT JOIN Examinations e 
    ON s.student_id = e.student_id 
    AND subj.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, subj.subject_name
ORDER BY s.student_id, subj.subject_name;

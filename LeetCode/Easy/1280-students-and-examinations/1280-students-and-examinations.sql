SELECT s.student_id, s.student_name, sb.subject_name, COUNT(ex.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sb
LEFT JOIN Examinations ex
    ON s.student_id = ex.student_id
    AND sb.subject_name = ex.subject_name
GROUP BY s.student_id, s.student_name, sb.subject_name
ORDER BY s.student_id, sb.subject_name
SELECT ROUND(AVG(g.grade)) AS average_score
FROM Grades AS g
JOIN Students AS st ON g.student_id = st.id
JOIN Subjects AS s ON g.subject_id = s.id
JOIN Teachers AS t ON s.teacher_id = t.id
WHERE st.name = 'Melissa Lindsey' 
  AND t.name = 'Fernando Vincent';

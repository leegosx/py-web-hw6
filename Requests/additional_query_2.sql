SELECT st.name AS Student, g.grade AS Grade
FROM Grades AS g
JOIN Students AS st ON g.student_id = st.id
JOIN Subjects AS s ON g.subject_id = s.id
JOIN Groups AS gr ON st.group_id = gr.id
WHERE gr.name = '3'
  AND s.name = 'Music Theory'
  AND g.date = (
    SELECT MAX(g_inner.date)
    FROM Grades AS g_inner
    WHERE g_inner.subject_id = s.id
  );


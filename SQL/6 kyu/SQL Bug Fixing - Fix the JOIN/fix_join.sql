SELECT j.job_title,
       round(SUM(j.salary) / COUNT(p.id), 2)::FLOAT AS average_salary,
       COUNT(p.id)::INT                             AS total_people,
       round(SUM(j.salary), 2)::FLOAT               AS total_salary
FROM people p
         LEFT JOIN job j ON p.id = j.people_id
GROUP BY j.job_title
ORDER BY average_salary DESC
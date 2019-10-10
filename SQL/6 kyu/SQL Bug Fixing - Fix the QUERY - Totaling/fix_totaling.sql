SELECT s.transaction_date::date AS day,
       d.name::text as department,
       COUNT(s.id)::INT as sale_count
FROM department d
    JOIN sale s ON d.id = s.department_id
GROUP BY day, department
ORDER BY day
SELECT id, name
FROM departments
WHERE id IN (
    SELECT department_id
    FROM sales
    WHERE price > 98.00
    )
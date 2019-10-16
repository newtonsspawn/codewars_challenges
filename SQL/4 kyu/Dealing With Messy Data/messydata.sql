SELECT
    c.first_name,
    c.last_name,
    c.credit_limit      AS old_limit,
    max(p.credit_limit) AS new_limit
FROM
    customers c,
    prospects p
WHERE
      p.full_name ILIKE '%' || c.first_name || '%'
  AND p.full_name ILIKE '%' || c.last_name || '%'
  AND c.credit_limit < p.credit_limit
GROUP BY
    c.first_name, c.last_name, c.credit_limit
ORDER BY
    first_name;
SELECT
    date(created_at) AS day,
    description,
    count(*)         AS count
FROM
    events
WHERE
    name = 'trained'
GROUP BY
    date(created_at),
    description
ORDER BY
    day,
    description
WITH
    cte_1 AS (
        SELECT
            to_char(date(created_at), 'YYYY-MM-01') AS date,
            count(*)::FLOAT                         AS count
        FROM
            posts
        GROUP BY
            date
        ORDER BY
            date),
    cte_2 AS (
        SELECT
            date,
            count,
            lag(count, 1) OVER (ORDER BY date) AS prev_month
        FROM
            cte_1
        ORDER BY
            date
    )
SELECT
    date::DATE,
    count::INT,
    to_char((((count - prev_month) / prev_month) * 100),
            'FM9990.0%') AS percent_growth
FROM
    cte_2
ORDER BY
    date
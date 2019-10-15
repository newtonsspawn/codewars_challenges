WITH
    post_count AS (SELECT
                       date(created_at) AS date,
                       count(*)::INT    AS count
                   FROM
                       posts
                   GROUP BY
                       date
                   ORDER BY
                       date)
SELECT
    date,
    count,
    sum(count) OVER (ORDER BY date) AS total
FROM
    post_count
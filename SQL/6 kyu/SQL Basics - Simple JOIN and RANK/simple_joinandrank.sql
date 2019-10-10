WITH joined AS (
    SELECT
           people.id as id,
           people.name as name,
           count(sales.sale) as sale_count
    FROM people
        LEFT JOIN sales ON people.id=sales.people_id
    GROUP BY people.id
)

SELECT
       id,
       name,
       sale_count,
       rank() OVER (ORDER BY sale_count) sale_rank
FROM joined

WITH
    act_105 AS (
        SELECT
            film_id
        FROM
            film_actor
        WHERE
            actor_id = 105
    )
SELECT DISTINCT
    title
FROM
    film                      f
        INNER JOIN film_actor fa ON f.film_id = fa.film_id
WHERE
      fa.actor_id = 122
  AND f.film_id IN (
    SELECT
        film_id
    FROM
        act_105)
ORDER BY title;
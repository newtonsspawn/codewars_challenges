WITH
    cte_01 AS (
        SELECT
            fa1.actor_id       AS first_actor_id,
            fa2.actor_id       AS second_actor_id,
            count(fa1.film_id) AS movie_count
        FROM
            film_actor                fa1
                INNER JOIN film_actor fa2 ON fa1.actor_id != fa2.actor_id
                AND fa1.film_id = fa2.film_id
        GROUP BY
            first_actor_id,
            second_actor_id
        ORDER BY
            movie_count DESC,
            first_actor_id
        LIMIT 1),
    cte_02 AS (
        SELECT
            fa1.actor_id AS first_actor_id,
            fa2.actor_id AS second_actor_id,
            fa1.film_id  AS movie_id
        FROM
            film_actor                fa1
                INNER JOIN film_actor fa2 ON fa1.actor_id != fa2.actor_id
                AND fa1.film_id = fa2.film_id
                INNER JOIN cte_01 ON cte_01.first_actor_id = fa1.actor_id
        WHERE
              fa1.actor_id = cte_01.first_actor_id
          AND fa2.actor_id = cte_01.second_actor_id)
SELECT
    a1.first_name || ' ' || a1.last_name AS first_actor,
    a2.first_name || ' ' || a2.last_name AS second_actor,
    film.title AS title
FROM
    cte_02
        INNER JOIN film ON cte_02.movie_id = film.film_id
        INNER JOIN actor a1 ON cte_02.first_actor_id = a1.actor_id
        INNER JOIN actor a2 ON cte_02.second_actor_id = a2.actor_id
ORDER BY
    title;
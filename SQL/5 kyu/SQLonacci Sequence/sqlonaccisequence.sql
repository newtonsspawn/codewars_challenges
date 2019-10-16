WITH
    RECURSIVE
    fib(number, next_num) AS (
        SELECT
            0::BIGINT,
            1::BIGINT
        UNION ALL
        SELECT
            next_num::BIGINT,
            number + next_num::BIGINT
        FROM
            fib
    )
SELECT
    number
FROM
    fib
LIMIT 90
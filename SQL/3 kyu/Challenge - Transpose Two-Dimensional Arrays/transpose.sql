SELECT
    array_agg(v ORDER BY j) matrix
FROM
    (
        SELECT
            rn,
            j,
            array_agg(v ORDER BY i) AS v
        FROM
            (
                SELECT
                    rn,
                    i,
                    j,
                    matrix[i][j] AS v
                FROM
                    (
                        SELECT
                            generate_subscripts(matrix, 2) j,
                            q.*
                        FROM
                            (
                                SELECT
                                    ROW_NUMBER() OVER ()           AS rn,
                                    generate_subscripts(matrix, 1) AS i,
                                    matrix
                                FROM
                                    matrices
                            ) q
                    ) r
            ) s
        GROUP BY rn, j
    ) t
GROUP BY
    rn
ORDER BY
    rn;
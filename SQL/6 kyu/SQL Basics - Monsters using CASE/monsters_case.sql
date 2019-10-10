SELECT
       t.id as id,
       t.heads as heads,
       t.arms as arms,
       b.legs as legs,
       b.tails as tails,
CASE
    WHEN heads > arms then 'BEAST'
    WHEN tails > legs then 'BEAST'
    ELSE 'WEIRDO'
END AS species
FROM top_half t, bottom_half b
WHERE t.id = b.id
ORDER BY species
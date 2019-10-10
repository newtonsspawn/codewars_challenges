SELECT player_name,
       games,
       cast(round((hits + 0.0) / at_bats, 3) AS VARCHAR(5)) AS batting_average
FROM yankees
WHERE at_bats >= 100
ORDER BY batting_average DESC
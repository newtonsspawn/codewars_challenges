SELECT coalesce(nullif(clan, ''), '[no clan specified]') AS clan,
       sum(points)                                       AS total_points,
       count(name)                                       AS total_people,
       rank() OVER (ORDER BY sum(points) DESC)
FROM people
GROUP BY clan
ORDER BY total_points DESC
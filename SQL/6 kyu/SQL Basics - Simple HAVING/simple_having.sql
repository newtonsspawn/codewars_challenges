SELECT age, COUNT(*) as total_people FROM people
GROUP BY age
HAVING COUNT(*) >= 10
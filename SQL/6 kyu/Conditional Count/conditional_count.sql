SELECT extract(MONTH FROM payment_date)              AS month,
       count(amount)                                 AS total_count,
       sum(amount)                                   AS total_amount,
       count(CASE WHEN staff_id = 1 THEN amount END) AS mike_count,
       sum(CASE WHEN staff_id = 1 THEN amount END)   AS mike_amount,
       count(CASE WHEN staff_id = 2 THEN amount END) AS jon_count,
       sum(CASE WHEN staff_id = 2 THEN amount END)   AS jon_amount
FROM payment
GROUP BY month
ORDER BY month
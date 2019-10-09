SELECT
       customer.customer_id,
       customer.email,
       COUNT(payment.customer_id)::INT as payments_count,
       SUM(payment.amount)::FLOAT as total_amount
FROM customer, payment
WHERE customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY total_amount DESC
LIMIT 10
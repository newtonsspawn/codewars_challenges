SELECT id,
       coalesce(nullif(name, ''), '[product name not found]')   AS name,
       price,
       coalesce(nullif(card_name, ''), '[card name not found]') AS card_name,
       card_number,
       transaction_date
FROM eusales
WHERE price IS NOT NULL
  AND price > 50.00
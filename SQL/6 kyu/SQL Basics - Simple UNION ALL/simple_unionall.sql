ALTER TABLE ussales
    ADD COLUMN location VARCHAR(200)
    DEFAULT 'US';

ALTER TABLE eusales
    ADD COLUMN location VARCHAR(200)
    DEFAULT 'EU';

SELECT * FROM ussales
    WHERE price > 50.00
UNION ALL
SELECT * FROM eusales
    WHERE price > 50.00
ORDER BY location DESC, id
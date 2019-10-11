CREATE FUNCTION agecalculator(date TIMESTAMP)
    RETURNS INTEGER AS
$$
BEGIN
    RETURN (
        SELECT EXTRACT(
            YEAR FROM age(date)
            )
        )::INT;
END;
$$ LANGUAGE plpgsql;
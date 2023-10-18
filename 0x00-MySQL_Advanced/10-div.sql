-- A function that divides numbers
DELIMITER //
CREATE FUNCTION SaveDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
	IF b = 0
		THEN RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END //

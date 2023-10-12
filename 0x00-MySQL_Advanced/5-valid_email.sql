-- create trigger to update the valid email slot after email changes
DELIMITER $$
CREATE TRIGGER check_email BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email
		THEN
		SET valid_email = 0;
	END IF;
END;$$

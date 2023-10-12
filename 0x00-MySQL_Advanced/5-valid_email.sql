-- create trigger to update the valid email slot after email changes
DELIMITER $$
CREATE TRIGGER check_email AFTER UPDATE ON users FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email
		SET valid_email = 0
	END IF;
END;
$$

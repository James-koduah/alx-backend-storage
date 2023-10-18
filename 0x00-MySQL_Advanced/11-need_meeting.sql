-- Create a view for some students who need a meeting
CREATE VIEW need_meeting AS SELECT * FROM students
WHERE score < 80
AND last_meeting IS null
OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH);


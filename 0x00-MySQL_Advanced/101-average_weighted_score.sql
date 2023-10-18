-- Compute average score for all students
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
	BEGIN
		UPDATE users,
			(SELECT users.id, SUM(score * weight) / SUM(weight) AS wei_avg
				FROM users
				JOIN corrections ON users.id = corrections.user_id
				JOIN projects ON projects.id = corrections.project_id
				GROUP BY users.id)
			AS weighted_avg
		SET users.average_score = weighted_avg.wei_avg
		WHERE users.id = weighted_avg.id;
	END //

-- Create a mysql index on two columns
CREATE INDEX idx_name_first_score on names(name(1), score);

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Get the state_id of California from the states table
SET @state_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of California sorted by cities.id
SELECT * FROM cities WHERE state_id = @state_id ORDER BY id ASC;

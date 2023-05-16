-- Specify the database name

USE hbtn_0c_0; 

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' -- Specify the database name
  AND TABLE_NAME = 'first_table'; -- Specify the table name

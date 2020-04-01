-- script that prepares a MySQL server for the project:
-- Create a hbnb_test_db if this doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Change de current database to hbnb_test_db
USE hbnb_test_db;
-- Create a new user if this doesn't exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Set a password for last user created
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Set all privileges for the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- I don't understand this line
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

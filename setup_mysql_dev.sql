-- script that prepares a MySQL server for the project:
-- Create a hbnb_dev_db if this doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Change de current database to hbnb_dev_db
USE hbnb_dev_db;
-- Create a new user if this doesn't exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Set a password for last user created
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Set all privileges for the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- I don't understand this line
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

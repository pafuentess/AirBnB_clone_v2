-- script that prepares a MySQL server for the project:

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
UPDATE mysql.user SET authentication_string=PASSWORD('hbnb_test_pwd') WHERE User='hbnb_test';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

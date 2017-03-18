-- create a database name hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- drops user if database exists
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
-- creates a user with user:hbnb_dev@localhost with pass hbnb_dev_pwd
CREATE USER 'hbnb_dev'@'localhost'IDENTIFIED BY 'hbnb_dev_pwd';
-- gives power to grant privileges to root user
UPDATE mysql.user SET Grant_priv='Y', Super_priv='Y' WHERE User='root';
FLUSH PRIVILEGES;
-- grant user hbnb_dev all privileges to database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* to 'hbnb_dev'@'localhost'

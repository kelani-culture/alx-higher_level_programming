-- a script that create a database and a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFY BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- set Grant for user_0d_2
GRANT ALL SELECT hbtn_0d_2 TO 'user_0d_2'@'localhost';

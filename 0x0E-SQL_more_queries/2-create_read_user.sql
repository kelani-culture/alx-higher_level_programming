-- create database and user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2 and grant privileges on the hbtn_0d_2 database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT hbtn_0d_2.* TO 'user_0d_2'@'localhost';

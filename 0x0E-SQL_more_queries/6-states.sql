-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the database created
USE hbtn_0d_usa;

-- create a table
CREATE TABLE IF NOT EXISTS states(
  id INT NOT NULL UNIQUE AUTO INCREMENT
  name VARCHAR(256) NOT NULL,
 PRIMARY KEY(id),
);

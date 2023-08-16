-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create a table
CREATE TABLE IF NOT EXISTS states(
  id INT NOT NULL AUTO INCREMENT,
  name VARCHAR(256),
  PRIMARY KEY(id)
);

-- create a table and Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the Database
USE hbtn_0d_usa;

-- create a table cities
CREATE TABLE cities(
  id INT NOT NULL PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY(state_id) REFERENCES states(id)
)

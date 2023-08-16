-- select all cities in carlifornia
USE hbtn_0d_usa;

-- select all cities in carlifornia
SELECT cities.id as id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;

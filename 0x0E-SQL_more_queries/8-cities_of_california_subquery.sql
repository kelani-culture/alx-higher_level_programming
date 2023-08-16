-- select all cities in carlifornia
SELECT cities.id as id, cities.name
FROM cities, states
WHERE states.name = "Carlifornia"
ORDER BY cities.id ASC;

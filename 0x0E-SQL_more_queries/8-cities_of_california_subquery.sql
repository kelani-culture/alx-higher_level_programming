-- select all cities in carlifornia
SELECT cities.id, cities.name
FROM states, cities
WHERE states.name = "California"
ORDER BY cities.id 

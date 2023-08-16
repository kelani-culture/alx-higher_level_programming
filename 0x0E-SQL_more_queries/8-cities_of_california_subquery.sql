-- select all cities in carlifornia
SELECT cities.id, cities.name
FROM states, cities
WHERE states.name = "California" and state_id = 1
ORDER BY cities.id 

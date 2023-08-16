-- select all cities in carlifornia
SELECT id, cities
FROM states, cities
WHERE name = "California"
ORDER BY cities.id 

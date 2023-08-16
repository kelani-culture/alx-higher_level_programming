-- select all cities in carlifornia
SELECT id, name
FROM states, cities
WHERE name = "California"
ORDER BY cities.id 

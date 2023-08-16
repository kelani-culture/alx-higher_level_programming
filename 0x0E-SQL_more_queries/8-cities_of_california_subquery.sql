-- select all cities in carlifornia
SELECT id, cities
FROM states
WHERE name = "California"
ORDER BY cities.id 

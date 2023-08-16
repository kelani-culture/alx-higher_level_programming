-- script that select all title dexter genre from database
-- hbtn_0d_tvshows

USE hbtn_0d_tvshows;
SELECT tv_genres.name as name
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY names;

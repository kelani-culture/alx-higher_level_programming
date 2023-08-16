-- list genres

SELECT tv_genres.name as genre, count(*) as number_of_shows
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL AND tv_show_genres.show_id IS NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC

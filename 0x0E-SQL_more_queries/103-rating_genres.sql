-- calculate ther rating of each genres
SELECT name, SUM(rate) AS rating
FROM tv_genres AS tv_g
JOIN tv_show_genres AS tv_sg ON tv_sg.genre_id = tv_g.id
JOIN tv_show_ratings AS tv_sr ON tv_sr.show_id = tv_sg.show_id
GROUP BY name
ORDER BY rating DESC

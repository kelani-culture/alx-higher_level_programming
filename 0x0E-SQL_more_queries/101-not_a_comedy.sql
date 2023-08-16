-- list tables genres not linked to dexter

SELECT DISTINCT title
  FROM tv_shows as tvs
  LEFT JOIN tv_show_genres as tvsg
    ON tvsg.show_id = tvs.id
  LEFT JOIN tv_genres as tvg ON tvsg.genre_id = tvg.id

  WHERE title NOT IN ( SELECT title
        FROM tv_shows as tvs
        LEFT JOIN tv_show_genres as tvsg
          ON tvsg.show_id = tvs.id
        LEFT JOIN tv_genres as tvg ON tvsg.genre_id = tvg.id
 
        WHERE name = "Comedy"
  )
  ORDER BY title

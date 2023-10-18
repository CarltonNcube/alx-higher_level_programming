-- Lists all genres not linked to the show Dexter in the hbtn_0d_tvshows database
SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;

-- script that uses the hbtn_0d_tvshows database to list
-- all genres not linked to the show Dexter

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS 'rating'
	FROM tv_genres
INNER JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_show_ratings
	ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY name
ORDER BY rating DESC;

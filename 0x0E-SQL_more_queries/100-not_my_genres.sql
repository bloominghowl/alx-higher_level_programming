-- Use the hbtn_0d_tvshows database

-- Get the genre IDs linked to the show Dexter
SELECT genre_id
FROM tv_show_genres
WHERE show_id = (
    SELECT id
    FROM tv_shows
    WHERE title = 'Dexter'
)

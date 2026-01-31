SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Genre JOIN Album JOIN Artist 
On Track.genre_id = Genre.id and Track.album_id = Album.id
and Album.artist_id = Artist.id
order by Artist.name LIMIT 3
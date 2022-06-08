from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = """INSERT INTO artists (name)
    VALUES (%s) RETURNING *
    """
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(
            row['name']
        )
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artist WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        artist = Artist(
            result['name']
        )
    return artist

def update(artist):
    sql = "UPDATE albums SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
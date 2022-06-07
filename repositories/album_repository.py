from db.run_sql import run_sql

from models.album import Album


def save(album):
    sql = """INSERT INTO albums (title, genre, artist_id)
    VALUES (%s, %s, %s) RETURNING id
    """
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    

def select(id):
    pass

def update(album):
    pass

def delete_all():
    pass

def delete(id):
    pass
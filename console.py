import pdb

from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

nirvana = Artist('Nirvana')
artist_repository.save(nirvana)

rage_atm = Artist('Rage Against The Machine')
artist_repository.save(rage_atm)

album_1 = Album('Nevermind', 'Rock', nirvana)
album_repository.save(album_1)
album_2 = Album('Bleach', 'Rock', nirvana)
album_repository.save(album_2)

album_3 = Album('Battle for Los Angeles', 'Rock', rage_atm)
album_repository.save(album_3)
album_4 = Album('Evil Empire', 'Rock', rage_atm)
album_repository.save(album_4)


pdb.set_trace()
from sqlalchemy import Column, Integer, ForeignKey, Table
from models.session import Base

# Association table for the many-to-many relationship between Playlist and Song
playlist_song_table = Table(
    'playlist_song',
    Base.metadata,
    Column('playlist_id', Integer, ForeignKey('playlists.id', ondelete='CASCADE'), primary_key=True),
    Column('song_id', Integer, ForeignKey('songs.id', ondelete='CASCADE'), primary_key=True)
)


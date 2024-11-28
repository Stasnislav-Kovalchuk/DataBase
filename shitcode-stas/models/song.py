from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.session import Base


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    duration = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False)

    # Many-to-many relationship to Playlist
    playlists = relationship('Playlist', secondary='playlist_song', back_populates='songs')

    def __repr__(self):
        return f"<Song(id={self.id}, title='{self.title}', genre='{self.genre}')>"

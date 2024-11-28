from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.session import Base
from datetime import datetime


class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    user = relationship('User', back_populates='playlists')

    # Many-to-many relationship to Song
    songs = relationship('Song', secondary='playlist_song', back_populates='playlists')

    def __repr__(self):
        return f"<Playlist(id={self.id}, name='{self.name}', user_id={self.user_id})>"

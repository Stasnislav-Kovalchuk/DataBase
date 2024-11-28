from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.session import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    email = Column(String(45), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now, nullable=False)

    # Relationship to Playlist
    playlists = relationship('Playlist', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

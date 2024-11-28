from models import playlist_song
from models.song import Song
from models.playlist import Playlist
from models.session import SessionLocal
from flask import abort


class SongsService:
    @staticmethod
    def get_all_songs():
        """Отримати всі пісні"""
        session = SessionLocal()
        songs = session.query(Song).all()  # Використовуй Song, а не song
        session.close()
        return songs

    @staticmethod
    def get_song_by_id(id: int):
        """Отримати пісню за ID"""
        session = SessionLocal()
        song = session.query(Song).where(Song.id == id).first()
        if not song:
            abort(404, description="Song not found")
        session.close()
        return song

    @staticmethod
    def create_song(title: str, duration: int, genre: str):
        """Створити нову пісню"""
        session = SessionLocal()
        new_song = Song(title=title, duration=duration, genre=genre)  # Використовуй Song
        session.add(new_song)
        session.commit()
        session.refresh(new_song)
        session.close()
        return new_song

    @staticmethod
    def update_song(
            song_id: int,
            title: str,
            duration: int,
            genre: str
    ):
        session = SessionLocal()
        song = session.query(Song).where(Song.id == song_id).first()
        if not song:
            abort(404, description="Song not found")
        song.title = title
        song.duration = duration
        song.genre = genre
        session.commit()
        return SongsService.get_song_by_id(song_id)

    @staticmethod
    def delete_song(
            song_id: int,
    ):
        session = SessionLocal()
        song = session.query(Song).where(Song.id == song_id).first()
        if not song:
            abort(404, description="Song not found")
        session.delete(song)
        session.commit()


from models.playlist import Playlist
from models.song import Song
from models.playlist_song import playlist_song_table
from models.user import User
from models.session import SessionLocal
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from flask import abort


class PlaylistsService:
    @staticmethod
    def get_all_playlists():
        """Отримати всі плейлисти"""
        with SessionLocal() as session:
            playlists = session.query(Playlist) \
                .options(selectinload(Playlist.user)) \
                .options(selectinload(Playlist.songs)).all()
            return playlists

    @staticmethod
    def get_playlist_by_id(id: int):
        """Отримати плейлист за ID"""
        with SessionLocal() as session:
            playlist = session.query(Playlist).where(Playlist.id == id) \
                .options(selectinload(Playlist.user)) \
                .options(selectinload(Playlist.songs)).first()
            if not playlist:
                raise abort(404, description="Playlist not found")
            return playlist

    @staticmethod
    def create_playlist(name: str, user_id: int):
        """Створити новий плейлист"""
        with SessionLocal() as session:
            user = session.query(User).get(user_id)
            if not user:
                abort(404, description="User not found")
            new_playlist = Playlist(name=name, user_id=user_id)
            session.add(new_playlist)
            session.commit()
            session.refresh(new_playlist)
        return PlaylistsService.get_playlist_by_id(new_playlist.id)

    @staticmethod
    def delete_playlist(id: int):
        """Видалити плейлист"""
        with SessionLocal() as session:
            playlist = session.query(Playlist).get(id)
            if not playlist:
                raise abort(404, description="Playlist not found")
            session.delete(playlist)
            session.commit()

    @staticmethod
    def add_song_to_playlist(playlist_id: int, song_id: int):
        """Додати пісню до плейлиста"""
        session = SessionLocal()
        playlist = session.query(Playlist).get(playlist_id)
        song = session.query(Song).get(song_id)

        # Перевірка на існування плейлиста та пісні
        if not playlist:
            session.close()
            abort(404, description="Playlist not found")
        if not song:
            session.close()
            abort(404, description="Song not found")

        # Додавання запису в проміжну таблицю
        stmt = playlist_song_table.insert().values(playlist_id=playlist_id, song_id=song_id)
        try:
            session.execute(stmt)
        except IntegrityError:
            abort(409, description="Song is already in playlist")
        session.commit()
        session.close()
        return PlaylistsService.get_playlist_by_id(playlist_id)

    @staticmethod
    def remove_song_from_playlist(playlist_id: int, song_id: int):
        """Remove a song from a playlist"""
        session = SessionLocal()

        # Check if the playlist and song exist
        playlist = session.query(Playlist).get(playlist_id)
        song = session.query(Song).get(song_id)
        if not playlist:
            session.close()
            abort(404, description="Playlist not found")
        if not song:
            session.close()
            abort(404, description="Song not found")

        # Delete the record from the association table
        stmt = playlist_song_table.delete().where(
            playlist_song_table.c.playlist_id == playlist_id,
            playlist_song_table.c.song_id == song_id
        )
        result = session.execute(stmt)

        # Check if any rows were deleted (if not, the song was not in the playlist)
        if result.rowcount == 0:
            session.close()
            abort(404, description="Song is not in the playlist")

        session.commit()
        session.close()
        return PlaylistsService.get_playlist_by_id(playlist_id)

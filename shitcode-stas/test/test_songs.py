import pytest
from services.songs import SongsService


def test_create_song(session):
    """Перевіряє створення пісні"""
    song = SongsService.create_song(title="Test Song", duration=180, genre="Pop")
    assert song.title == "Test Song"
    assert song.duration == 180
    assert song.genre == "Pop"

def test_get_all_songs(session):
    """Перевіряє отримання всіх пісень"""
    songs = SongsService.get_all_songs()
    assert len(songs) > 0

def test_add_song_to_playlist(session):
    """Перевіряє додавання пісні до плейлиста"""
    playlist_id = 1  # Переконайся, що є плейлист із ID 1
    song = SongsService.create_song(title="Another Song", duration=200, genre="Rock")
    SongsService.add_song_to_playlist(playlist_id=playlist_id, song_id=song.id)

    songs_in_playlist = SongsService.get_songs_in_playlist(playlist_id)
    assert song.id in [s.id for s in songs_in_playlist]

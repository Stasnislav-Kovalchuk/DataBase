import pytest
from services.playlists import PlaylistsService

def test_create_playlist(session):
    """Перевіряє створення плейлиста"""
    playlist = PlaylistsService.create_playlist(name="Test Playlist", user_id=1)
    assert playlist.name == "Test Playlist"
    assert playlist.user_id == 1

def test_get_all_playlists(session):
    """Перевіряє отримання всіх плейлистів"""
    playlists = PlaylistsService.get_all_playlists()
    assert len(playlists) > 0

def test_get_playlist_by_id(session):
    """Перевіряє отримання плейлиста за ID"""
    playlist = PlaylistsService.create_playlist(name="Another Playlist", user_id=1)
    retrieved_playlist = PlaylistsService.get_playlist_by_id(playlist.id)
    assert retrieved_playlist.id == playlist.id
    assert retrieved_playlist.name == "Another Playlist"

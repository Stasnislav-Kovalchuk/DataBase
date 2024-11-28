from typing import List
from schemas.playlist_schema import PlaylistDTO
from schemas.user_schema import UserDTO
from schemas.song_schema import SongDTO


class RUserDTO(UserDTO):
    playlists: List[PlaylistDTO]


class RPlaylistDTO(PlaylistDTO):
    user: UserDTO
    songs: List[SongDTO]

from pydantic import BaseModel


class PlaylistBase(BaseModel):
    name: str
    user_id: int

    class Config:
        from_attributes = True


class PlaylistDTO(PlaylistBase):
    id: int


class CreatePlaylistDTO(PlaylistBase):
    pass


class AddSongDTO(BaseModel):
    song_id: int

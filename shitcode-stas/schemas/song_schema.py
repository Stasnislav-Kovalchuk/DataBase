from pydantic import BaseModel
from typing import List, Optional

class SongDTO(BaseModel):
    id: int
    title: str
    duration: int
    genre: str

    class Config:
        from_attributes = True  # Дозволяє використовувати SQLAlchemy ORM-об'єкти

class CreateSongDTO(BaseModel):
    title: str
    duration: int
    genre: str

class UpdateSongDTO(BaseModel):
    title: Optional[str] = None
    duration: Optional[int] = None
    genre: Optional[str] = None

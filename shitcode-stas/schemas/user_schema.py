from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import List


class UserBase(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # Дозволяє використовувати SQLAlchemy ORM-об'єкти


class UserDTO(UserBase):
    id: int
    registration_date: datetime


class CreateUserDTO(UserBase):
    pass


class UpdateUserDTO(UserBase):
    pass

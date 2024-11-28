from models.user import User
from models.session import SessionLocal
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload


class UserService:
    @staticmethod
    def get_all_users():
        """Отримати всіх користувачів"""
        session = SessionLocal()
        users = session.query(User).options(selectinload(User.playlists)).all()
        session.close()
        return users

    @staticmethod
    def get_user_by_id(id: int):
        """Отримати користувача за ID"""
        session = SessionLocal()
        user = session.query(User).options(selectinload(User.playlists)).get(id)
        session.close()
        return user

    @staticmethod
    def create_user(name: str, email: str):
        """Створити нового користувача"""
        session = SessionLocal()
        new_user = User(name=name, email=email)
        session.add(new_user)
        try:
            session.commit()
        except IntegrityError:
            raise BadRequest("User already exists")
        session.refresh(new_user)
        session.close()
        return UserService.get_user_by_id(new_user.id)

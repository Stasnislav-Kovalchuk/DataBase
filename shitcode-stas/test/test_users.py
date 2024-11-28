import pytest
from models.user import User
from services.users import UserService


def test_create_user(session):
    """Перевіряє створення користувача"""
    user = UserService.create_user(name="Test User", email="test@example.com")
    assert user.name == "Test User"
    assert user.email == "test@example.com"

def test_get_all_users(session):
    """Перевіряє отримання всіх користувачів"""
    users = UserService.get_all_users()
    assert len(users) > 0

def test_get_user_by_id(session):
    """Перевіряє отримання користувача за ID"""
    user = UserService.create_user(name="Another User", email="another@example.com")
    retrieved_user = UserService.get_user_by_id(user.id)
    assert retrieved_user.id == user.id
    assert retrieved_user.email == "another@example.com"

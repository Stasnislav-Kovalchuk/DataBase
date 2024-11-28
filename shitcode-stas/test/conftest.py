import pytest
from main import app
from models.session import Base, engine, SessionLocal

# Фікстура для тестового клієнта Flask
@pytest.fixture(scope="module")
def test_client():
    """Фікстура для тестового клієнта Flask"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            yield client  # Це дозволяє використовувати клієнт для тестування

# Фікстура для бази даних
@pytest.fixture(scope="module")
def init_database():
    """Фікстура для ініціалізації бази даних перед тестами"""
    # Створення таблиць для тестів
    Base.metadata.create_all(bind=engine)
    yield
    # Видалення таблиць після тестів
    Base.metadata.drop_all(bind=engine)

# Фікстура для сесії
@pytest.fixture(scope="function")
def session():
    """Фікстура для сесії SQLAlchemy для кожного тесту"""
    db_session = SessionLocal()  # Створюємо нову сесію
    yield db_session  # Додаємо сесію для використання в тестах
    db_session.rollback()  # Оскільки ми тестуємо, скидаємо зміни після тесту
    db_session.close()  # Закриваємо сесію після тесту

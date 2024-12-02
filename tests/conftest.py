import pytest
from app import create_app
from app.database import db

@pytest.fixture
def app():
    """
    Configura una instancia de la aplicación Flask para pruebas.
    """
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # Base de datos en memoria para pruebas
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with app.app_context():
        db.create_all()  # Crear las tablas necesarias en memoria
        yield app  # Proporciona la aplicación para las pruebas
        """ db.session.remove()
        db.drop_all()  """ # Limpia la base de datos después de las pruebas


@pytest.fixture
def client(app):
    """
    Proporciona un cliente de pruebas para enviar solicitudes HTTP.
    """
    return app.test_client()


@pytest.fixture
def book_data():
    """
    Fixture con datos simulados de un libro.
    """
    return {
        "id": "592fbe9897ba43ca801d57d99d6361c2",
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "read": True
    }
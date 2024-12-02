import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from app.books.routes import book_blueprint
from app.books.services import create_book


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(book_blueprint, url_prefix='/books')
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()


def test_create_book_with_mock():
    # Datos simulados
    book_data = {
        "title": "On the Road",
        "author": "Jack Kerouac",
        "read": True
    }


    with patch("app.books.services.Books") as MockBooks, \
         patch("app.books.services.db.session") as mock_session:

        mock_book_instance = MagicMock()
        mock_book_instance.title = book_data["title"] 
        MockBooks.return_value = mock_book_instance

        response = create_book(book_data)

        MockBooks.assert_called_once_with(
            title="On the Road",
            author="Jack Kerouac",
            read=True
        )


        mock_session.add.assert_called_once_with(mock_book_instance)
        mock_session.commit.assert_called_once()

        assert response["message"] == "New book On the Road was created"

def test_add_book_validation_error(client):
    invalid_data = {"author": "Jack Kerouac"}

    with patch("app.books.services.create_book") as mock_create_book:
        response = client.post('/books/', json=invalid_data)
        json_data = response.get_json()

        assert response.status_code == 400
        assert "errors" in json_data
        mock_create_book.assert_not_called()


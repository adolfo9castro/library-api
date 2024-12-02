from unittest.mock import patch, MagicMock
from app.books.services import get_all_books, create_book, get_book_by_id

def test_create_book_with_mock(book_data):
   
    with patch("app.database.db.session") as mock_session:
        mock_session.add = MagicMock()
        mock_session.commit = MagicMock()

   
        response = create_book(book_data)

       
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()


        assert response["message"] == f"New book {book_data['title']} was created"


def test_get_all_books_with_mock(app):
  
    with app.app_context():
        
        with patch("app.models.Books.query") as mock_query:
            mock_query.all.return_value = [
                MagicMock(id="592fbe9897ba43ca801d57d99d6361c2", title="On the Road", author="Jack Kerouac", read=True),
                MagicMock(id="5c499541d2694ddf949ba6f730ff2863", title="Green Eggs and Ham", author="Dr. Seuss", read=False)
            ]

         
            books = get_all_books()

            assert len(books) == 2
            assert books[0]["id"] == "592fbe9897ba43ca801d57d99d6361c2"
            assert books[0]["title"] == "On the Road"
            assert books[0]["author"] == "Jack Kerouac"
            assert books[0]["read"] is True
            assert books[1]["id"] == "5c499541d2694ddf949ba6f730ff2863"
            assert books[1]["title"] == "Green Eggs and Ham"
            assert books[1]["author"] == "Dr. Seuss"
            assert books[1]["read"] is False

            
            mock_query.all.assert_called_once()


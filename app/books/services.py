from app.models import Books
from app.database import db


def create_book(data):
    new_book = Books(
        title=data.get('title'),
        author=data.get('author'),
        read=data.get('read')
    )
    db.session.add(new_book)
    db.session.commit()
    return {"message": f"New book {new_book.title} was created"}

def get_all_books():
    books = Books.query.all()
    return [{
        "id": book.id, 
        "title": book.title, 
        "author": book.author,
        "read": book.read
    } for book in books]


def get_book_by_id(id):
    print(id)
    book = Books.query.get(id)
    if not book:
        return None
    return {
        "id": book.id, 
        "title": book.title,
        "author": book.author,
        "read": book.read
    }


def edit_book(id, data):
    book = Books.query.get(id)
    if not book:
        return None
    
    book.title = data.get('title')
    book.author = data.get('author')
    book.read = data.get('read')
    db.session.commit()    
    return {"message":f"{book.title} was updated successfull"}


def delete_book(id):
    book = Books.query.get(id)
    if not book:
        return None
    
    db.session.delete(book)
    db.session.commit()    
    return {'message':f'{book.title} was deleted successfull'}

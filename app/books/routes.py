from flask import request, jsonify, current_app as app
from marshmallow import ValidationError
from app.books import book_blueprint
from app.books.services import create_book, get_all_books, get_book_by_id, edit_book, delete_book
from app.books.schemas import BooksSchema
from app.database import db

book_schema = BooksSchema()

@book_blueprint.route('/', methods=['POST'])
def add_book():
    """
    Create a new book
    ---
    tags:
      - Books
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              description: Book title
            author:
              type: string
              description: Book author
            read:
              type: boolean
              description: Read status
    responses:
      201:
        description: Book successfully created
      400:
        description: Missing or invalid parameters
      500:
        description: Internal server error
    """    
    try:
        data = book_schema.load(request.get_json())
        new_book = create_book(data)
        app.logger.info(f"create a book {new_book}")
        return jsonify(new_book), 201
    except ValidationError as error:
        db.session.rollback()
        app.logger.error(f"Error missing paremeter")
        return jsonify({"errors": error.messages}), 400
    except Exception as error:
        db.session.rollback()
        app.logger.error(error)
        return jsonify({"error": 'Internal Error'}), 500
    finally:
        db.session.close()

@book_blueprint.route('/', methods=['GET'])
def list_books():
    """
    Retrieve all books
    ---
    tags:
      - Books
    responses:
      200:
        description: List of books
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              title:
                type: string
              author:
                type: string
              read:
                type: boolean
    """
    books = get_all_books()
    app.logger.info("get all books")
    return jsonify(books), 200


@book_blueprint.route('/<string:id>', methods=['GET'])
def get_book(id):
    """
    Retrieve a book by ID
    ---
    tags:
      - Books
    parameters:
      - name: id
        in: path
        required: true
        type: string
        description: Book ID (UUID)
    responses:
      200:
        description: Book found
        schema:
          type: object
          properties:
            id:
              type: string
            title:
              type: string
            author:
              type: string
            read:
              type: boolean
      404:
        description: Book not found
    """
    book = get_book_by_id(id)
    app.logger.info("Get book by id")
    if not book:
        return jsonify({"error": "book not found"}), 404
    return jsonify(book), 200


@book_blueprint.route('/<string:id>', methods=['PUT'])
def put_book(id):
    """
    Update a book
    ---
    tags:
      - Books
    parameters:
      - name: id
        in: path
        required: true
        type: string
        description: Book ID (UUID)
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              description: New book title
            author:
              type: string
              description: New book author
            read:
              type: boolean
              description: New read status
    responses:
      200:
        description: Book successfully updated
      404:
        description: Book not found
      500:
        description: Internal server error
    """      
    try:
        data = book_schema.load(request.get_json())
        book = edit_book(id, data)
        if not book:
            return jsonify({'error':'book not found'}), 404
        app.logger.info(book)
        return jsonify(book), 200
    except ValidationError as error:
        db.session.rollback()
        app.logger.error("Error missing paremeter")
        return jsonify({'error':error.messages}), 500
    finally:
        db.session.close()

@book_blueprint.route('/<string:id>', methods=['DELETE'])
def remove_book(id):
    """
    Delete a book
    ---
    tags:
      - Books
    parameters:
      - name: id
        in: path
        required: true
        type: string
        description: Book ID (UUID)
    responses:
      200:
        description: Book successfully deleted
      404:
        description: Book not found
      500:
        description: Internal server error
    """
        
    try:
        book = delete_book(id)
        if not book:
            return jsonify({'error':'book not found'}), 404
        
        app.logger.info("Deleted book")
        return jsonify(book), 200
    except Exception as error:
        db.session.rollback()
        app.logger.error(error)
        return jsonify({'error':error}), 500
    finally:
        db.session.close()
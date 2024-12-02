from flask import Blueprint

book_blueprint = Blueprint('books', __name__)

from . import routes
from flask import Flask
from flasgger import Swagger

from dotenv import load_dotenv
from app.logging_config import logging_config
from app.config import Config
from app.database import init_db
from app.extensions import init_extensions
from app.middleware import init_middlewares
from app.books import book_blueprint

def create_app(config_class=Config):
    
    logging_config()
    
    load_dotenv(override=True)

    app = Flask(__name__)
    
    app.config['SWAGGER'] = {
        'title': 'Library API',
        'uiversion': 3
    }
    swagger = Swagger(app)
    
    app.config.from_object(config_class)

    init_extensions(app)

    init_db(app)
    
    init_middlewares(app)

    app.register_blueprint(book_blueprint, url_prefix='/books')

    return app
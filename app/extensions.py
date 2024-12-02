from flask_cors import CORS
import os

def init_extensions(app):
    cors = CORS(app, resources={r"/*": {
        "origins": {os.getenv('ORIGINS')},
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Authorization", "Content-Type"],
        "supports_credentials": True
    }})
    cors.init_app(app)

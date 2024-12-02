from flask_cors import CORS
import os

def init_extensions(app):
    cors = CORS(app, resources={r"/*": {
        "origins": {os.getenv('ORIGINS')},
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Authorization", "Content-Type"],
        "supports_credentials": True  # Permite el envío de cookies si es necesario
    }})
    cors.init_app(app)  # Habilitar CORS
    #jwt.init_app(app)
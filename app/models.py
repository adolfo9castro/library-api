from app.database import db
import uuid

class Books(db.Model):
    __tablename__='register'

    id = db.Column(db.String(32), default=lambda: uuid.uuid4().hex, primary_key=True, nullable=False)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), unique=False, nullable=False)
    read = db.Column(db.Boolean, nullable=False)
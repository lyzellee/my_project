from models.db import db
from datetime import datetime, timezone


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(200))
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc),
    onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<User {self.uname}>"

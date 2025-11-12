from models.db import db
from datetime import datetime, timezone


class User(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    uname = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True)
    pass_word = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<User {self.uname}>"

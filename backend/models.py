from datetime import datetime as dt

from backend import db


class URLModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1024), unique=True, nullable=False)
    shortened_url = db.Column(db.String(50), unique=True, nullable=False)
    counter = db.Column(db.Integer, nullable=False, default=1)
    date = db.Column(db.DateTime, nullable=False, default=dt.utcnow())

    def __repr__(self) -> str:
        return f"URLs('{self.original_url}', '{self.shortened_url}' '{self.date}')"

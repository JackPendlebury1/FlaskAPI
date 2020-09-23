from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)
    genre = db.Column(db.String(20))
    image = db.Column(db.LargeBinary)
    release = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    description = db.Column(db.String(255))
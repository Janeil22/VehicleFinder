from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(150))
    model = db.Column(db.String(150))
    years = db.Column(db.String(100))
    transmission = db.Column(db.String(150))
    cmg = db.Column(db.String(100))
    hmg = db.Column(db.String(100))
    drive = db.Column(db.String(100))
    engine = db.Column(db.String(100))
    c = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    searches = db.relationship('Search')





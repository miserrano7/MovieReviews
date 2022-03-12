from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(120))
    rating = db.Column(db.String(120))
    movieIDs = db.Column(db.Integer)
    user_name = db.Column(db.String(120))

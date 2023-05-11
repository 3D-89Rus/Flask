from flask_login import UserMixin

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(25), unique=True)
    name = db.Column(db.String(25))
    password = db.Column(db.String(25))

    def __init__(self, email, password):
        self.email = email
        self.password = password


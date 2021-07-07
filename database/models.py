from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Gender(db.Document):
    username = db.StringField(required=True, unique=True)
    gender = db.StringField(required=True)
    age = db.StringField(required=True)


class Users(db.Document):
    name = db.StringField(required=True)
    surname = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Influencer(db.Document):
    username = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    follower = db.IntField(required=True)
    genderM = db.IntField(required=True)
    genderF = db.IntField(required=True)
    age = db.ListField(required=True)


class Admin(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

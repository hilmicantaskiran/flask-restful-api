from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Register(db.Document):
    name = db.StringField(required=True)
    surname = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class GenderAge(db.Document):
    username = db.StringField(required=True, unique=True)
    gender = db.StringField(required=True)
    age = db.StringField(required=True)


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

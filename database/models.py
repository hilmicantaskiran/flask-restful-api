from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class UserName(db.Document):
    username = db.StringField(required=True, unique=True)


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


User.register_delete_rule(UserName, 'added_by', db.CASCADE)

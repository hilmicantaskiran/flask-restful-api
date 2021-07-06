from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_HOST'] = 'mongodb+srv://hilmican:dpmd1930@intern.51qqm.mongodb.net/intern?retryWrites=true&w=majority'

initialize_db(app)
initialize_routes(api)


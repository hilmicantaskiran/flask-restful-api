from flask import request
from database.models import Users
from flask_restful import Resource
from mongoengine.errors import DoesNotExist
from resources.errors import EmailUnauthorizedError, InternalServerError


class RegisterLoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = Users.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                return {'error': 'Email or password invalid'}, 400
            else:
                id = authorized.id
                return {'id': str(id)}, 200

        except (EmailUnauthorizedError, DoesNotExist):
            raise EmailUnauthorizedError
        except Exception:
            raise InternalServerError

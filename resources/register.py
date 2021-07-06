from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Register
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, ValidationError
from resources.errors import SchemaValidationError, UserNameAlreadyExistsError, InternalServerError


class RegisterApi(Resource):
    def get(self):
        user_name = Register.objects().to_json()
        return Response(user_name, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            body = request.get_json(force=True)
            user_name = Register(**body).save()
            id = user_name.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise UserNameAlreadyExistsError
        except Exception:
            raise InternalServerError

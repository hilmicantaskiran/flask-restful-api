from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Register
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, UpdatingUserNameError, DeletingUserNameError, \
    UserNameNotExistsError


class RegisterGetApi(Resource):
    def get(self):
        user_name = Register.objects().to_json()
        return Response(user_name, mimetype="application/json", status=200)


class RegisterApi(Resource):
    @jwt_required()
    def put(self, email):
        try:
            body = request.get_json(force=True)
            Register.objects.get(email=email).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingUserNameError
        except Exception:
            raise InternalServerError

    @jwt_required()
    def delete(self, email):
        try:
            Register.objects.get(email=email).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingUserNameError
        except Exception:
            raise InternalServerError

    def get(self, email):
        try:
            user_name = Register.objects.get(email=email).to_json()
            return Response(user_name, mimetype="application/json", status=200)
        except DoesNotExist:
            raise UserNameNotExistsError
        except Exception:
            raise InternalServerError

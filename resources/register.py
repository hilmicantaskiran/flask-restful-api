from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Register
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, \
    UpdatingUserNameError, DeletingUserNameError, UserNameNotExistsError, EmailAlreadyExistsError


class RegisterGetPostApi(Resource):
    def get(self):
        email = Register.objects().to_json()
        return Response(email, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            body = request.get_json(force=True)
            email = Register(**body).save()
            id = email.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception:
            raise InternalServerError


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
            user_email = Register.objects.get(email=email).to_json()
            return Response(user_email, mimetype="application/json", status=200)
        except DoesNotExist:
            raise UserNameNotExistsError
        except Exception:
            raise InternalServerError
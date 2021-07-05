from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import GenderAge
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, UserNameAlreadyExistsError, InternalServerError, \
    UpdatingUserNameError, DeletingUserNameError, UserNameNotExistsError


class GendersAgesApi(Resource):
    def get(self):
        genders = GenderAge.objects().to_json()
        return Response(genders, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            body = request.get_json(force=True)
            gender = GenderAge(**body).save()
            id = gender.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise UserNameAlreadyExistsError
        except Exception:
            raise InternalServerError


class GenderAgeApi(Resource):
    @jwt_required()
    def put(self, username):
        try:
            body = request.get_json(force=True)
            GenderAge.objects.get(username=username).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingUserNameError
        except Exception:
            raise InternalServerError

    @jwt_required()
    def delete(self, username):
        try:
            GenderAge.objects.get(username=username).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingUserNameError
        except Exception:
            raise InternalServerError

    def get(self, username):
        try:
            gender = GenderAge.objects.get(username=username).to_json()
            return Response(gender, mimetype="application/json", status=200)
        except DoesNotExist:
            raise UserNameNotExistsError
        except Exception:
            raise InternalServerError

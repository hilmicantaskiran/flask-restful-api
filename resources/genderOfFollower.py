from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import GenderOfFollower
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, UserNameAlreadyExistsError, InternalServerError, \
    UpdatingUserNameError, DeletingUserNameError, UserNameNotExistsError


class GenderOfFollowersApi(Resource):
    @jwt_required()
    def get(self):
        gender = GenderOfFollower.objects().to_json()
        return Response(gender, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            body = request.get_json(force=True)
            inf = GenderOfFollower(**body).save()
            id = inf.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise UserNameAlreadyExistsError
        except Exception:
            raise InternalServerError


class GenderOfFollowerApi(Resource):
    @jwt_required()
    def put(self, username):
        try:
            body = request.get_json(force=True)
            GenderOfFollower.objects.get(username=username).update(**body)
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
            GenderOfFollower.objects.get(username=username).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingUserNameError
        except Exception:
            raise InternalServerError

    @jwt_required()
    def get(self, username):
        try:
            gender = GenderOfFollower.objects.get(username=username).to_json()
            return Response(gender, mimetype="application/json", status=200)
        except DoesNotExist:
            raise UserNameNotExistsError
        except Exception:
            raise InternalServerError

class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class UserNameAlreadyExistsError(Exception):
    pass


class UpdatingUserNameError(Exception):
    pass


class DeletingUserNameError(Exception):
    pass


class UserNameNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "MovieAlreadyExistsError": {
        "message": "Username with given name already exists",
        "status": 400
    },
    "UpdatingMovieError": {
        "message": "Updating username added by other is forbidden",
        "status": 403
    },
    "DeletingMovieError": {
        "message": "Deleting username added by other is forbidden",
        "status": 403
    },
    "MovieNotExistsError": {
        "message": "Username with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}
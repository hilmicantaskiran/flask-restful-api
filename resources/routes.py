from resources.gender import GendersAgesApi, GenderAgeApi
from resources.register import RegisterApi
from resources.auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(GendersAgesApi, '/api/gender')
    api.add_resource(GenderAgeApi, '/api/gender/<username>')

    api.add_resource(RegisterApi, '/api/register')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')


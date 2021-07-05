from resources.gender import GendersAgesApi, GenderAgeApi
from resources.username import UserNamesApi, UserNameApi
from resources.auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(GendersAgesApi, '/api/gender')
    api.add_resource(GenderAgeApi, '/api/gender/<username>')

    api.add_resource(UserNamesApi, '/api/username')
    api.add_resource(UserNameApi, '/api/username/<username>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')


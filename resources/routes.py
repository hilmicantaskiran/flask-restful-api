from resources.inf import InfluencersApi, InfluencerApi
from resources.register import RegisterGetPostApi, RegisterApi
from resources.auth import SignupApi, LoginApi
from resources.login import RegisterLoginApi


def initialize_routes(api):
    api.add_resource(InfluencersApi, '/api/inf')
    api.add_resource(InfluencerApi, '/api/inf/<username>')

    api.add_resource(RegisterGetPostApi, '/api/user/register')
    api.add_resource(RegisterApi, '/api/user/register/<email>')

    api.add_resource(RegisterLoginApi, '/api/user/login')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

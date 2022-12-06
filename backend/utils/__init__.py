from api import api_bp,api
from api.tests import TestApi
from api.posts import PostApi
from api.auth import UserRegistrationApi, UserSignInApi

def add_apis():
    api.add_resource(TestApi, '/api/test')
    api.add_resource(UserRegistrationApi, '/api/register')
    api.add_resource(UserSignInApi, '/api/signin')
    api.add_resource(PostApi, '/api/articles') # contains posts and get 
    

def add_blueprints(app):
    app.register_blueprint(api_bp)

from flask_restful import Resource
from flask import request
from flask import jsonify
from importlib_metadata import pass_none
from models import User
        
class UserRegistrationApi(Resource):
    # impl usre registration
    # POST /api/register      
    def post(self):
        # get the post data
        pass


class UserSignInApi(Resource):
    # impl usre registration
    # POST /api/signin      
    def post(self):
        # get the post data
        pass
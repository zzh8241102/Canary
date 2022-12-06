import email
from hashlib import new
import json
from re import A
import re
from urllib import response
from flask_restful import Resource, reqparse
from flask import request,make_response
from flask import jsonify
from importlib_metadata import pass_none
from models import User
from forms import RegisterForm
# from controller.auth_controller import auth_controller
from werkzeug.datastructures import ImmutableMultiDict
# hash 密码加密
from werkzeug.security import check_password_hash, generate_password_hash


        
#//////////////////// init ////////////////////////
reg_parser = reqparse.RequestParser()
reg_parser.add_argument('username', type=str, required=True, help='username is required')
reg_parser.add_argument('password', type=str, required=True, help='password is required')
reg_parser.add_argument('email', type=str, required=True, help='email is required')
# auth_ctrl = auth_controller()
#//////////////////// init end ////////////////////////
class UserRegistrationApi(Resource):
    # impl usre registration
    # POST /api/register      
    def __init__(self):
        self.response_obj = {
                            'success': "false",
                            'message':{},
                            'code':0,
                            'data':{}
                            }
    def post(self):
        # get the post data
        data = reg_parser.parse_args()
        form = RegisterForm(ImmutableMultiDict(data))
        if(form.validate()==False):
            self.response_obj['message'] = 'Invalid form data.'
            self.response_obj['success'] = "false"
            return make_response(jsonify(self.response_obj), 401)
        if User.find_by_username(data['username']):
            self.response_obj['message'] = 'User already exists. Please Log in.'
            self.response_obj['code'] = 2
            self.response_obj['success'] = "false"
            return make_response(jsonify(self.response_obj), 400)
        new_user = User(user_email=data['email'],user_name=data['username'])
        password_encrypted = generate_password_hash(data['password'])
        new_user.user_password = password_encrypted
        try:
            new_user.save()
            self.response_obj['message'] = 'User created successfully.'
            self.response_obj['success'] = "true"
            self.response_obj['data'] = data['username']
            return make_response(jsonify(self.response_obj), 201)
        except:
            self.response_obj['message'] = 'Cannot Create User. Please try again later.'
            self.response_obj['success'] = "false"
            return make_response(jsonify(self.response_obj), 401)


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, help='username is required')
login_parser.add_argument('password', type=str, required=True, help='password is required')
class UserSignInApi(Resource):
    # impl usre registration
    # POST /api/signin      
    """
    SignIn api will return a json object with the following info:
        'code','success','data':{},'token':{} 
    """
    def __init__(self):
        self.response_obj = {
                            'success': "true", 
                            'message': "",
                            'code': 0, 
                            'data': {}, 
                            'token':{}
                            }
    def post(self):
        # get the post data
        data = login_parser.parse_args()
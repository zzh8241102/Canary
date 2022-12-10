from flask_restful import Resource, reqparse
from flask import request,make_response
from flask import jsonify
from models import User
from forms import RegisterForm,LoginForm
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
                            'data':{},
                            'session':''
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
            # get user id by username
            self.response_obj['session'] = data['username']
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
                            'token':{},
                            'session':''
                            }
    def post(self):
        # get the post data
        data = login_parser.parse_args()
        print(data)
        form = LoginForm(ImmutableMultiDict(data))
        print(form.data)
        print(form.validate())
        if(form.validate()==False):
            self.response_obj['message'] = 'Invalid form data.'
            self.response_obj['success'] = "false"
            return make_response(jsonify(self.response_obj), 401)
        if not User.find_by_username(data['username']):
            self.response_obj['message'] = 'User does not exist.'
            self.response_obj['success'] = "false"
            return make_response(jsonify(self.response_obj), 400)
        user = User.find_by_username(data['username'])
        if check_password_hash(user.user_password,data['password']):
            # generate the auth token
            # auth_token = user.encode_auth_token(user.user_id)
            # if auth_token:
            self.response_obj['message'] = 'User signed'
            self.response_obj['success'] = "true"
            self.response_obj['data'] = data['username']
            self.response_obj['session'] = data['username']
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['message'] = 'Password is wrong.'
            self.response_obj['success'] = "false"
            return make_response(jsonify(self.response_obj), 400)

# /api/user?user=username 
from flask_restful import Resource,reqparse
from models import User
from flask import request,make_response,jsonify
from controller.user_info_controller import fetch_user_info
from forms import UserBasicInfoForm
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.security import check_password_hash, generate_password_hash
# ///////////// init /////////////
user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='username is required')
# ///////////// init /////////////
# /api/user?username=username 
class UserInfoApi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            'data': {
                'user':{
                    'username':"",
                    'email':"",
                    'phoneNumber':"",
                    'location':"",
                },
            }
        }
    def get(self):
        data = user_parser.parse_args()
        if(User.find_by_username(data['username'])):
            # return the user info
            self.response_obj['data']['user']['username'] = fetch_user_info(username=data['username']).user_name 
            self.response_obj['data']['user']['email'] = fetch_user_info(username=data['username']).user_email
            self.response_obj['data']['user']['phoneNumber'] = fetch_user_info(username=data['username']).user_phone
            self.response_obj['data']['user']['location'] = fetch_user_info(username=data['username']).user_location
            self.response_obj['message'] = "User found."
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found."
            return make_response(jsonify(self.response_obj), 404)



user_chang_parser = reqparse.RequestParser()
user_chang_parser.add_argument('username', type=str, required=True, help='username is required')
user_chang_parser.add_argument('email', type=str, required=True, help='email is required')
user_chang_parser.add_argument('phoneNumber', type=str, required=True, help='phoneNumber is required')
user_chang_parser.add_argument('location', type=str, required=True, help='location is required')
# /api/user/change?username=username&email=email&phoneNumber=phoneNumber&location=location
class ChangeUserInfoAPi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            'data': {
                'user':{
                    'username':"",
                    'email':"",
                    'phoneNumber':"",
                    'location':"",
                },
            }
        }
    def post(self):
        data = user_chang_parser.parse_args()
        form = UserBasicInfoForm(ImmutableMultiDict(data))
        if not form.validate():
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "Invalid input."
            return make_response(jsonify(self.response_obj), 400)
        if(User.find_by_username(data['username'])):
            # return the user info
            user = User.query.filter_by(user_name=data['username']).first()
            user.user_email = data['email']
            user.user_phone = data['phoneNumber']
            user.user_location = data['location']
            user.save()
            self.response_obj['data']['user']['username'] = fetch_user_info(username=data['username']).user_name 
            self.response_obj['data']['user']['email'] = fetch_user_info(username=data['username']).user_email
            self.response_obj['data']['user']['phoneNumber'] = fetch_user_info(username=data['username']).user_phone
            self.response_obj['data']['user']['location'] = fetch_user_info(username=data['username']).user_location
            self.response_obj['message'] = "User info changed."
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found."
            return make_response(jsonify(self.response_obj), 404)

change_password_user_parser = reqparse.RequestParser()
change_password_user_parser.add_argument('username', type=str, required=True, help='username is required')
change_password_user_parser.add_argument('oldPassword', type=str, required=True, help='password is required')
change_password_user_parser.add_argument('newPassword', type=str, required=True, help='newPassword is required')
class ChangePasswordAPi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            }
    def post(self):
        data = change_password_user_parser.parse_args()
        if(User.find_by_username(data['username'])):
            # return the user info

            user = User.query.filter_by(user_name=data['username']).first()
            if(check_password_hash(user.user_password,data['oldPassword'])):
                user.user_password = generate_password_hash(data['newPassword'])
                user.save()
                self.response_obj['message'] = "Password changed."
                return make_response(jsonify(self.response_obj), 200)
            else:
                self.response_obj['success'] = "false"
                self.response_obj['message'] = "Old Password not match."
                return make_response(jsonify(self.response_obj), 400)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found."
            return make_response(jsonify(self.response_obj), 404)

delete_user_parser = reqparse.RequestParser()
delete_user_parser.add_argument('username', type=str, required=True, help='username is required')

class DeleteAccountApi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            }
    def post(self):
        data = delete_user_parser.parse_args()
        if(User.find_by_username(data['username'])):
            # return the user info
            user = User.query.filter_by(user_name=data['username']).first()
            # delete the user
            user.delete(user.user_name)
            self.response_obj['message'] = "User deleted."
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found."
            return make_response(jsonify(self.response_obj), 404)


        
        
        
        
        
        
        
        
        
        

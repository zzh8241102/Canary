# /api/user?user=username 
from flask_restful import Resource,reqparse
from models import User
from flask import request,make_response,jsonify
from controller.user_info_controller import fetch_user_info

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
                    
                },
            }
        }
    def get(self):
        data = user_parser.parse_args()
        if(User.find_by_username(data['username'])):
            # return the user info
            self.response_obj['data']['user']['username'] = fetch_user_info(username=data['username']).user_name 
            self.response_obj['data']['user']['email'] = fetch_user_info(username=data['username']).user_email
            self.response_obj['message'] = "User found."
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found."
            return make_response(jsonify(self.response_obj), 404)
            


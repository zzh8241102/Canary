import imp
from urllib import response
from flask_restful import Resource, reqparse
from flask import request,make_response
from flask import jsonify,Response
import os
import time
from controller.upload_controller import find_user_avatar_by_user_name
from models import User
import cv2
# accept user uploaded avatar

# /api/upload/avatar
class UploadAvatarApi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            'data': {
                'avatar':"",
            }
        }
    def post(self):
        # file0 = request.form.get('fileToUpload') # request.form outputs ImmutableMultiDict([]); request.form.get('fileToUpload') outputs None
        file = request.files.getlist('fileToUpload')[0] # the type of file is FileStorage
        # reading the user_name from the request
        # transform the ImmutableMultiDict to dict
        request.form = request.form.to_dict()
        user_name = request.form.get('username')
        filename = file.filename
        # filename 加上不重复的时间戳
        s= str(time.time())
        s = s.replace('.','')
        filename = s + filename
        # 转换file storage 为图片
        file.save(os.getcwd()+'/upload/avatar/'+filename)
        url_stored = os.getcwd()+'/upload/avatar/'+filename
        print(url_stored)
        # 存到User model里的 avatar_url
        # 找到对应user_name的user
        user = User.query.filter_by(user_name=user_name).first()
        user.user_avatar = url_stored
        user.save()
        # 返回url
        self.response_obj['data']['avatar'] = url_stored
        return make_response(jsonify(self.response_obj), 200)
        


# ///// user_name_for_avatar ////////////////////////
# /api/find/avatar
user_find_avatar_parser = reqparse.RequestParser()
user_find_avatar_parser.add_argument('username', type=str, required=True, help='username is required')
# ////////////////////////////////////////////////
class FindAvatarApi(Resource):
    def get(self):
        # reading the user_name from the request
        # transform the ImmutableMultiDict to dict
        data = user_find_avatar_parser.parse_args()
        user_name = data['username']
        # find the avatar url
        avatar_url = find_user_avatar_by_user_name(user_name)
        # read the image
        image_data = open(avatar_url, "rb").read()
        response = make_response(image_data)
        # header 支持jpg和png两种类型
        response.headers['Content-Type'] = 'image/jpg'
        response.headers['Content-Type'] = 'image/png'
        
        return make_response(response, 200)


        

        
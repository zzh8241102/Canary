import imp
from flask_restful import Resource, reqparse
from flask import request,make_response
from flask import jsonify,Response
import os
import time
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
        

class FindAvatarApi(Resource):
    # /api/find/avatar?=username
    # return the blob of the avatar

    # this interface will read the username, and find the avatar url in the database
    # then return the blob of the avatar
    def get(self):
        # get the username from the request
        # transform the ImmutableMultiDict to dict
        request.args = request.args.to_dict()
        user_name = request.args.get('username')
        # find the avatar url in the database
        user = User.query.filter_by(user_name=user_name).first()
        url_stored = user.user_avatar
        # read the img by base64
        # return the blob of the avatar ,which can be rendered by el-avatar
        mdict = {
        'jpeg': "image/joeg",
        'jpg' : 'image/jpg',
        'png' : 'image/png',
        }
        mine = mdict[url_stored.split('.')[-1]]
        return Response(url_stored, mimetype=mine)
        

        
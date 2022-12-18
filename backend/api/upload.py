import imp
from flask_restful import Resource, reqparse
from flask import request,make_response,jsonify
from extension import logger
import os
import time
from controller.upload_controller import find_user_avatar_by_user_name
from models import User
from utils.decors import login_required

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
    @login_required
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
        # 存到User model里的 avatar_url
        # 找到对应user_name的user
        user = User.query.filter_by(user_name=user_name).first()
        user.user_avatar = url_stored
        user.save()
        # 返回url
        self.response_obj['data']['avatar'] = url_stored
        logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{} {}'.format(request.remote_addr,request.method,request.path,200,"User avatar uploaded successfully, user name is ",user_name))
        return make_response(jsonify(self.response_obj), 200)
        


# ///// user_name_for_avatar ////////////////////////
# /api/find/avatar
user_find_avatar_parser = reqparse.RequestParser()
user_find_avatar_parser.add_argument('username', type=str, required=True, help='username is required')
# ////////////////////////////////////////////////
class FindAvatarApi(Resource):
    @login_required
    def get(self):
        # reading the user_name from the request
        # transform the ImmutableMultiDict to dict
        data = user_find_avatar_parser.parse_args()


        user_name = data['username']

        if(User.find_by_username(user_name) is None):
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found"
            self.response_obj['code'] = 1
            logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{} {}').format(request.remote_addr,request.method,request.path,404,"User not found when updating the avatar, user name is ",user_name)
            return make_response(jsonify(self.response_obj), 404)
        # find the avatar url
        avatar_url = find_user_avatar_by_user_name(user_name)
        # read the image
        image_data = open(avatar_url, "rb").read()
        response = make_response(image_data)
        # header 支持jpg和png两种类型
        response.headers['Content-Type'] = 'image/jpg'
        response.headers['Content-Type'] = 'image/png'
        
        logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{} {}'.format(request.remote_addr,request.method,request.path,200,"User avatar found successfully, user name is ",user_name))

        return make_response(response, 200)



        

        
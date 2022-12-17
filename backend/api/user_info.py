# /api/user?user=username 
#////////////////////////////////////////////////////////////////////////
from flask_restful import Resource,reqparse
from models import Article,Tags_Mid,Tags,Comments,Likes,User
from flask import request,make_response,jsonify
from controller.user_info_controller import fetch_user_info
from controller.like_controller import fetch_article_like_num,fetch_article_comment_num
from controller.tag_controller import find_article_by_tag_name,find_article_tags
from forms import UserBasicInfoForm
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.security import check_password_hash, generate_password_hash

# ////////////////////////////////////////////////////////////////////////
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


#///////////////////// change user info ///////////////////////
user_chang_parser = reqparse.RequestParser()
user_chang_parser.add_argument('username', type=str, required=True, help='username is required')
user_chang_parser.add_argument('email', type=str, required=True, help='email is required')
user_chang_parser.add_argument('phoneNumber', type=str, required=True, help='phoneNumber is required')
user_chang_parser.add_argument('location', type=str, required=True, help='location is required')
#///////////////////// change user info ///////////////////////
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

#///////////////////////// change password //////////////////////////
change_password_user_parser = reqparse.RequestParser()
change_password_user_parser.add_argument('username', type=str, required=True, help='username is required')
change_password_user_parser.add_argument('oldPassword', type=str, required=True, help='password is required')
change_password_user_parser.add_argument('newPassword', type=str, required=True, help='newPassword is required')
#/////////////////////////// change password //////////////////////////
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


#///////////////////////// user activity //////////////////////////
user_activity_parser = reqparse.RequestParser()
user_activity_parser.add_argument('user_name', type=str, required=True, help='username is required')
user_activity_parser.add_argument('is_commented', type=str, required=True, help='activity is required')
user_activity_parser.add_argument('is_liked', type=str, required=True, help='activity is required')
user_activity_parser.add_argument('is_published', type=str, required=True, help='activity is required')
#/////////////////////////// user activity //////////////////////////
class UserActivityInfoApi(Resource):
    # fetch user activity info
    # return the user activity info according to the request
    # and 
    def __init__(self):
        self.response_obj = {
            'message': "successfully get the articles list",
            'code': 0,
            'data':
            {
                'articles':[]
            },
        }
    def get(self):

        data = user_activity_parser.parse_args()
        if data['is_commented'] == 'true' and data['is_liked'] == 'false' and data['is_published'] == 'false':
            # fetch the articles commented by the user
            # from the comment table,find the article id according to the user name
            # and find the article info according to the article id
            comments = Comments.query.filter_by(comment_author=data['user_name']).all()
            # find the article info according to the article id in these comments
            articles = []
            for comment in comments:
                article_found = Article.query.filter_by(article_id=comment.comment_article).first()
                if article_found not in articles and article_found is not None:
                    articles.append(article_found)   
    
            for article in articles:
                tags = find_article_tags(article_id=article.article_id)
                # find the tags for the article
                p_time = article.published_time
                # change the published time to the format of 2022-11-11
                p_time = p_time.strftime("%Y-%m-%d")
                self.response_obj['data']['articles'].append(
                {
                    'id': article.article_id,
                    'title': article.article_title,
                    'author': article.article_author,
                    'date': p_time,
                    'comment': fetch_article_comment_num(article_id=article.article_id),
                    'like': fetch_article_like_num(article_id=article.article_id),
                    'tags':tags
                })
            return make_response(jsonify(self.response_obj), 200)
        if data['is_liked'] == 'true' and data['is_commented'] == 'false' and data['is_published'] == 'false':
            # fetch the articles liked by the user
            # from the like table,find the article id according to the user name
            # and find the article info according to the article id
            likes = Likes.query.filter_by(like_corr_user=data['user_name']).all()
            # find the article info according to the article id in these comments
            articles = []
            for like in likes:
                article_found = Article.query.filter_by(article_id=like.like_corr_article).first()
                if article_found not in articles and article_found is not None:
                    articles.append(article_found)   
            for article in articles:
                tags = find_article_tags(article_id=article.article_id)
                # find the tags for the article
                p_time = article.published_time
                # change the published time to the format of 2022-11-11
                p_time = p_time.strftime("%Y-%m-%d")
                self.response_obj['data']['articles'].append(
                {
                    'id': article.article_id,
                    'title': article.article_title,
                    'author': article.article_author,
                    'date': p_time,
                    'comment': fetch_article_comment_num(article_id=article.article_id),
                    'like': fetch_article_like_num(article_id=article.article_id),
                    'tags':tags
                })
            return make_response(jsonify(self.response_obj), 200)
        
        if(data['is_published'] == 'true' and data['is_commented'] == 'false' and data['is_liked'] == 'false'):
            # fetch the articles published by the user
            # from the article table,find the article id according to the user name
            # and find the article info according to the article id
            articles = Article.query.filter_by(article_author=data['user_name']).all()
            for article in articles:
                tags = find_article_tags(article_id=article.article_id)
                # find the tags for the article
                p_time = article.published_time
                # change the published time to the format of 2022-11-11
                p_time = p_time.strftime("%Y-%m-%d")
                self.response_obj['data']['articles'].append(
                {
                    'id': article.article_id,
                    'title': article.article_title,
                    'author': article.article_author,
                    'date': p_time,
                    'comment': fetch_article_comment_num(article_id=article.article_id),
                    'like': fetch_article_like_num(article_id=article.article_id),
                    'tags':tags
                })
            return make_response(jsonify(self.response_obj), 200)
            

#///////////////////////// user info stats //////////////////////////
user_info_stats_parser = reqparse.RequestParser()
user_info_stats_parser.add_argument('username', type=str, required=True, help='username is required')
#/////////////////////////// user info stats //////////////////////////

class UserInfoStatsApi(Resource):
    # get the user info stats
    # count on how many does the user commented, published, liked
    def __init__(self):
        self.response_obj = {
            'message': "successfully get the user info stats",
            'code': 0,
            'data':
            {
                'commented':0,
                'published':0,
                'liked':0
            },
        }
    def get(self):
        data = user_info_stats_parser.parse_args()
        # if user exists
        if not User.find_by_username(data['username']):
            return make_response(jsonify({'message': 'user not found', 'code': 1}), 404)

        # fetch the user info stats
        # from the comment table,find the article id according to the user name
        # and find the article info according to the article id
        comments = Comments.query.filter_by(comment_author=data['username']).all()
        # find the article info according to the article id in these comments
        articles = []
        for comment in comments:
            article_found = Article.query.filter_by(article_id=comment.comment_article).first()
            if article_found not in articles and article_found is not None:
                articles.append(article_found)
        self.response_obj['data']['commented'] = len(articles)
        # fetch the user info stats
        # from the like table,find the article id according to the user name
        # and find the article info according to the article id
        likes = Likes.query.filter_by(like_corr_user=data['username']).all()
        # find the article info according to the article id in these comments
        articles = []
        for like in likes:
            article_found = Article.query.filter_by(article_id=like.like_corr_article).first()
            if article_found not in articles and article_found is not None:
                articles.append(article_found)
        self.response_obj['data']['liked'] = len(articles)
        # fetch the user info stats
        # from the article table,find the article id according to the user name
        # and find the article info according to the article id
        articles = Article.query.filter_by(article_author=data['username']).all()
        self.response_obj['data']['published'] = len(articles)
        return make_response(jsonify(self.response_obj), 200)



            
            
        
        
        
        
        
        
        

# contains all the api for tags
# tag page
# api/tags
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import Tags, User, Article, UserTags
from controller.tag_controller import find_article_by_tag_name, find_article_tags

# class TagApi(Resource):
#     def get(self):
#         pass
# /api/tags?user=username

# ///////////////////////////////////////////////////////////////
tag_user_api_parser = reqparse.RequestParser()
tag_user_api_parser.add_argument(
    'username', type=str, required=True, help='username is required')
# ///////////////////////////////////////////////////////////////


class TagUserApi(Resource):
    def __init__(self):
        self.response_obj_sample = {
            'tags': [

            ]
        }

    def get(self):
        # find the user's all tags by the usertag mid level table
        data = tag_user_api_parser.parse_args()
        user_name = data['username']
        # check if the user exists
        if not User.find_by_username(user_name):
            return make_response(jsonify({'message': 'user not found'}), 404)
        user_id = User.getUserIdByName(user_name)
        userTag = UserTags.query.filter_by(user_id=user_id).all()
        for tag in userTag:
            self.response_obj_sample['tags'].append(
                tag.tag.tag_name)
        # find all the tags on userTag
        return make_response(jsonify(self.response_obj_sample), 200)


# //////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////
class AllTagsApi(Resource):
    def __init__(self):
        self.response_obj_sample = {
            'tags': [

            ]
        }

    def get(self):
        # fetch all the tags from the database
        tags = Tags.query.all()
        for tag in tags:
            self.response_obj_sample['tags'].append({
                'tag_id': tag.tag_id,
                'tag_name': tag.tag_name,
                'tag_description': tag.tag_description,
            })

        return make_response(jsonify(self.response_obj_sample), 200)


# ////////////////////////// add new tag //////////////////////////
new_tag_parser = reqparse.RequestParser()
new_tag_parser.add_argument(
    'tag_name', type=str, required=True, help='username is required')
new_tag_parser.add_argument(
    'tag_description', type=str, required=True, help='username is required')
# ///////////////////////// add new tag //////////////////////////


class AddNewTagApi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
        }

    def post(self):
        print("add new tag")
        data = new_tag_parser.parse_args()
        # check if the tag already exist
        # add the tag to the database
        if(data['tag_name'] not in [tag.tag_name for tag in Tags.query.all()]):
            new_tag = Tags(tag_name=data['tag_name'],
                           tag_description=data['tag_description'])
            new_tag.save()
            self.response_obj['message'] = "successfully add the tag"
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "tag already exist"
            return make_response(jsonify(self.response_obj), 404)


# ///////////////////////// find article's tag //////////////////////////
find_article_tag_parser = reqparse.RequestParser()
find_article_tag_parser.add_argument(
    'article_id', type=str, required=True, help='username is required')
# ///////////////////////// find article's tag //////////////////////////


class FindArticleTagApi(Resource):
    def __init__(self):
        self.response_obj_sample = {
            'tags': [

            ]
        }

    def get(self):
        # fetch all the tags from the database
        data = find_article_tag_parser.parse_args()
        tags = find_article_tags(data['article_id'])
        for tagname in tags:
            self.response_obj_sample['tags'].append({
                'tag_name': tagname,
            })

        return make_response(jsonify(self.response_obj_sample), 200)


# ////////////////////////////////////////////////////////////////////
find_tag_two_parser = reqparse.RequestParser()
find_tag_two_parser.add_argument(
    'tag_id', type=str, required=True, help='username is required')
# ////////////////////////////////////////////////////////////////////


class FindTaginfoByTagNameAPi(Resource):
    def __init__(self):
        self.response_obj_sample = {
            'tag_info': {
                'tag_id': 0,
                'tag_name': '',
                'tag_description': '',
            }
        }

    def get(self):
        data = find_tag_two_parser.parse_args()
        tag_id = data['tag_id']
        # fetch all the tags from the database
        tag = Tags.query.filter_by(tag_id=tag_id).first()
        if(tag is not None):
            self.response_obj_sample['tag_info']['tag_id'] = tag.tag_id
            self.response_obj_sample['tag_info']['tag_name'] = tag.tag_name
            self.response_obj_sample['tag_info']['tag_description'] = tag.tag_description
            return make_response(jsonify(self.response_obj_sample), 200)
        else:
            return make_response(jsonify(self.response_obj_sample), 404)


# ////////////////////////////////////////////////////////////////////
user_follow_tag_parser = reqparse.RequestParser()
user_follow_tag_parser.add_argument(
    'user_name', type=str, required=True, help='username is required')
user_follow_tag_parser.add_argument(
    'tag_id', type=str, required=True, help='tag is required')
# ////////////////////////////////////////////////////////////////////


class UserFollowTagApi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
        }

    def post(self):
        data = user_follow_tag_parser.parse_args()
        print(data)
        # check if the tag already exist
        # add the tag to the database
        print([tag.tag_id for tag in Tags.query.all()])
        if(int(data['tag_id']) not in [tag.tag_id for tag in Tags.query.all()]):
            print("tag not exist")
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "tag not exist"
            return make_response(jsonify(self.response_obj), 404)
        elif(data['user_name'] not in [user.user_name for user in User.query.all()]):
            print("user not exist")
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "user not exist"
            return make_response(jsonify(self.response_obj), 404)
        else:
            # user tag is the mid level table for the many to many relationship
            print(data['user_name'])
            # check if the user already follow the tag
            if(UserTags.query.filter_by(user_id=User.getUserIdByName(data['user_name']), tag_id=data['tag_id']).first() is not None):

                self.response_obj['success'] = "false"
                self.response_obj['message'] = "user already follow the tag"
                return make_response(jsonify(self.response_obj), 404)
            else:
                user_tag = UserTags(user_id=User.getUserIdByName(
                    data['user_name']), tag_id=data['tag_id'])
                user_tag.save()

# ////////////////////////////////////////////////////////////////////////////////////
tag_follower_list_parser = reqparse.RequestParser()
tag_follower_list_parser.add_argument('tag_id', type=str, required=True, help='tag is required')
# ////////////////////////////////////////////////////////////////////////////////////
class TagFollowerApi(Resource):
    def __init__(self):
        self.response_obj_sample = {
            'followers': [

            ]
        }

    def get(self):
        data = tag_follower_list_parser.parse_args()
        tag_id = data['tag_id']
        # fetch all the tags from the database
        followers = UserTags.query.filter_by(tag_id=tag_id).all()
        for follower in followers:
            print(follower.user_id)
            # query the user info by the user id
            # user avatar, user name, user id
            # find the user_reg_time in User table
            user_reg_time = User.query.filter_by(user_id=follower.user_id).first().user_reg_time
            self.response_obj_sample['followers'].append({
                'user_name': User.getUserNameById(follower.user_id),
                # 'user_avatar': User.getUserAvatarById(follower.user_id),
                'user_reg_time': user_reg_time.strftime('%Y-%m-%d %H:%M:%S'),
            })

        return make_response(jsonify(self.response_obj_sample), 200)
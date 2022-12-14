# contains all the api for tags
# tag page
# api/tags
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import Tags
from controller.tag_controller import find_article_by_tag_name, find_article_tags

# class TagApi(Resource):
#     def get(self):
#         pass
# /api/tags?user=username
class TagUserApi(Resource):
    def __init__(self):
        self.response_obj_sample = {
            'tags': [
                'llvm',
                'c++',
                'python',
                'torch',
                'java',
                'compiler',
                'machine learning',
                'data science',
            ]
        }
        
    def get(self):
        return make_response(jsonify(self.response_obj_sample), 200)

# api/addtag
class AddTagApi(Resource):
    def __init__(self):
    #     self.response_obj_sample = {
    #         'message': "successfully add the tag",
    #         'code': 0,
    #         'data': {
    #             'tag': 'c++',
    #         }
    #     }
        pass

        
    # def post(self):
    #     return make_response(jsonify(self.response_obj_sample), 200)

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
                'tag_name':tag.tag_name,
                'tag_description':tag.tag_description,
            })
            
        return make_response(jsonify(self.response_obj_sample), 200)

#////////////////////////// add new tag //////////////////////////
new_tag_parser = reqparse.RequestParser()
new_tag_parser.add_argument('tag_name', type=str, required=True, help='username is required')
new_tag_parser.add_argument('tag_description', type=str, required=True, help='username is required')
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
            new_tag = Tags(tag_name=data['tag_name'], tag_description=data['tag_description'])
            new_tag.save()
            self.response_obj['message'] = "successfully add the tag"
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "tag already exist"
            return make_response(jsonify(self.response_obj), 404)
        
# ///////////////////////// find article's tag //////////////////////////
find_article_tag_parser = reqparse.RequestParser()
find_article_tag_parser.add_argument('article_id', type=str, required=True, help='username is required')
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
                'tag_name':tagname,
            })
            
        return make_response(jsonify(self.response_obj_sample), 200)

# contains all the api for tags
# tag page
# api/tags
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import Tags

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
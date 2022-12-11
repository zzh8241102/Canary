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


new_tag_parser = reqparse.RequestParser()
new_tag_parser.add_argument('tag_name', type=str, required=True, help='username is required')
new_tag_parser.add_argument('tag_description', type=str, required=True, help='username is required')
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
        print(data)
        if(data['tag_name'] not in [tag.tag_name for tag in Tags.query.all()]):
            new_tag = Tags(tag_name=data['tag_name'], tag_description=data['tag_description'])
            new_tag.save()
            self.response_obj['message'] = "successfully add the tag"
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "tag already exist"
            return make_response(jsonify(self.response_obj), 404)
        



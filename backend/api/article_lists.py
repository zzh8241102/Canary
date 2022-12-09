# includes the all api for articles and
# the forms shoulb be like
# 1. /api/articleslist
# 2. /api/articleslist?tag=tagname
# 3. /api/articleslist?user=username

from cgi import print_form
import re
from flask_restful import Resource, reqparse
from flask import request, make_response
from flask import jsonify
from importlib_metadata import pass_none
from models import User


class ArticlesListApi(Resource):
    def __init__(self):
        # the return sample should be a list of articles, and for each article
        # each article have the 1. id 2. title 3. author 4. tags 5. date 6. number of comments
        # 7. number of likes
        self.response_obj_sample = {
            'message': "successfully get the articles list",
            'code': 0,
            'data': 
            {
                'articles':
                [
                    {
                        'id': 1,
                        'title': 'how to learn sklearn',
                        'author': 'author',
                        'tags': ['machine learning', 'python', 'data science'],
                        'date':'2022-11-11',
                        'comments':5,
                        'likes':10
                    },
                    {
                        'id': 2,
                        'title': 'how to resolve the problem of overfitting',
                        'author': 'author',
                        'tags': ['machine learning', 'python', 'deep learning'],
                        'date':'2022-12-9',
                        'comments':5,
                        'likes':11
                    },
                                     {
                        'id': 2,
                        'title': 'how to resolve the problem of overfitting',
                        'author': 'author',
                        'tags': ['machine learning', 'python', 'deep learning'],
                        'date':'2022-12-9',
                        'comments':5,
                        'likes':11
                    },
                                     {
                        'id': 2,
                        'title': 'how to resolve the problem of overfitting',
                        'author': 'author',
                        'tags': ['machine learning', 'python', 'deep learning'],
                        'date':'2022-12-9',
                        'comments':5,
                        'likes':11
                    },
                                     {
                        'id': 2,
                        'title': 'how to resolve the problem of overfitting',
                        'author': 'author',
                        'tags': ['machine learning', 'python', 'deep learning'],
                        'date':'2022-12-9',
                        'comments':5,
                        'likes':11
                    },
                ]
            }

        }

    def get(self):
        
        return make_response(jsonify(self.response_obj_sample), 200)

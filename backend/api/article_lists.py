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
from models import User,Article,Tags,Tags_Mid

def fetch_article_info():

    # fetch all the articles from the database,where the id, title author and date are fetched
    pass

    


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
                        'title': 'How to learn sklearn',
                        'author': 'jackie',
                        'tags': ['machine learning', 'python', 'data science'],
                        'date':'2022-11-11',
                        'comments':5,
                        'likes':10
                    },
                    {
                        'id': 2,
                        'title': 'How to resolve the problem of overfitting',
                        'author': 'yuheng',
                        'tags': ['machine learning', 'python', 'deep learning'],
                        'date':'2022-12-9',
                        'comments':5,
                        'likes':11
                    },
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'black',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },                                         
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'MarioSpr',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'MarioSpr',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },                                               
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'MarioSpr',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },                                               
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'MarioSpr',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },                                               
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'MarioSpr',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    }, 
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'MarioSpr',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },                                               
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'MarioSpr',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },                                        
                    {
                        'id': 2,
                        'title': 'How can use GDB',
                        'author': 'author',
                        'tags': ['GDB', 'c'],
                        'date':'2022-12-9',
                        'comments':15,
                        'likes':110
                    },

                ]
            }

        }
        self.response_obj = {
            'message': "successfully get the articles list",
            'code': 0,
            'data':
            {
                'articles':[]
            },
        }
    def get(self):
        articles = Article.query.all()
        # fetch all the tags from the database, notice the tag_mid is the model for many to many
        # relationship between tags and articles
        tag_mids = Tags_Mid.query.all()
        # for each article, fetch the tags using article id
        for article in articles:
            # fetch the tags for each article
            tags = []
            for tag_mid in tag_mids:
                if tag_mid.article_id == article.article_id:
                    tag_name = Tags.getTagNamebyId(tag_mid.tag_id)
                    tags.append(tag_name)
            # record the all the info into the response_obj_sample
            p_time = article.published_time
            # change the published time to the format of 2022-11-11
            p_time = p_time.strftime("%Y-%m-%d")
            self.response_obj['data']['articles'].append(
            {
                'id': article.article_id,
                'title': article.article_title,
                'author': article.article_author,
                'tags': tags,
                'date': p_time,
                'comments':999,
                'likes': 999,
            })
        return make_response(jsonify(self.response_obj), 200)

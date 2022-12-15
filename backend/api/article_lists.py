# includes the all api for articles and
# the forms shoulb be like
# 1. /api/articleslist
# 2. /api/articleslist?tag=tagname
# 3. /api/articleslist?user=username

from cgi import print_form
from flask_restful import Resource, reqparse
from flask import request, make_response
from flask import jsonify
from importlib_metadata import pass_none
from models import User,Article,Tags,Tags_Mid
from controller.tag_controller import find_article_by_tag_name, find_article_tags
from controller.like_controller import fetch_article_comment_num,fetch_article_like_num

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
                'comments': fetch_article_comment_num(article.article_id),
                'likes': fetch_article_like_num(article.article_id),
            })
        return make_response(jsonify(self.response_obj), 200)


#////////////////////////////////////////////////////////////////////////////////////////
article_list_tag_parser = reqparse.RequestParser()
article_list_tag_parser.add_argument('tag_id', type=str, required=True, help='tag is required')
#////////////////////////////////////////////////////////////////////////////////////////
class ArticleListByTagApi(Resource):
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
        data = article_list_tag_parser.parse_args()
        tag_id = data['tag_id']
        # for tags in Tags
        # we seek the tag in the tag_mid table
        # if the tag exists in the tag_mid table
        # we fetch the article id as a list
        tags = Tags()
        all_tags = tags.query.all()
        tags_mid = Tags_Mid().query.all()

        for tag in all_tags:
            print(int(tag_id))
            if int(tag_id) == tag.tag_id:
                print(tag_id)
                # tag_ = Tags_Mid.query.filter_by(tag_id=tag_id).all()
                # find all the tag_mid with the tag_id
                tag_ = Tags_Mid.query.filter_by(tag_id=tag_id).all()
                print(tag_)
                # return the corresponding article id as a list
                article_id_list = []
                for tag_mid in tag_:
                    article_id_list.append(tag_mid.article_id)
                article_list = [ Article.query.filter_by(article_id=article_id).first() for article_id in article_id_list]
                for article in article_list:
                    # fetch the tags for each article
                    tags = []
                    for tag_mid in tags_mid:
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
                        'comments': fetch_article_comment_num(article.article_id),
                        'likes': fetch_article_like_num(article.article_id),
                    })
                return make_response(jsonify(self.response_obj), 200)
                

                
            
                
                    



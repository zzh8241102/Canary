#  get the article content
# the article its self with the user comments
# /api/article?article_id=article_id

from flask_restful import Resource,reqparse
from models import Article
from flask import jsonify, make_response
from controller.article_controller import find_article_tags
from controller.like_controller import fetch_article_like_num
#/////////////////////////////////////////////
from utils.decors import login_required
article_content_parser = reqparse.RequestParser()
article_content_parser.add_argument('article_id', type=str, required=True, help='article_id is required')

#/////////////////////////////////////////////
class ArticleContentApi(Resource):
    def __init__(self):
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            'data': {
                'article':{
                    'article_id':"",
                    'article_title':"",
                    'article_content':"",
                    'article_author':"",
                    'article_tags':"",
                    'article_date':"",
                    'article_comments':[],
                    'article_likes':"",
                },
            }
        }
    @login_required
    def get(self):
        data = article_content_parser.parse_args()
        if(Article.find_by_article_id(data['article_id'])):
            article = Article.find_by_article_id(data['article_id'])
            self.response_obj['data']['article']['article_id'] = article.article_id
            self.response_obj['data']['article']['article_title'] = article.article_title
            self.response_obj['data']['article']['article_content'] = article.article_content
            self.response_obj['data']['article']['article_author'] = article.article_author
            self.response_obj['data']['article']['article_date'] = article.published_time 
            self.response_obj['data']['article']['article_tags'] = find_article_tags(data['article_id'])
            self.response_obj['data']['article']['article_comments'] = []
            self.response_obj['data']['article']['article_likes'] = fetch_article_like_num(data['article_id'])
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "Article not found."
            return make_response(jsonify(self.response_obj), 404)
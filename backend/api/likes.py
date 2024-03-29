from flask_restful import Resource,reqparse
from flask import jsonify, make_response,request
from numpy import array
from models import Article,User,Tags,Tags_Mid,Comments,Likes
from extension import logger
from utils.decors import login_required

#/////////////////////////////////////////////////////////////////
article_like_parser = reqparse.RequestParser()
article_like_parser.add_argument('article_id', type=str, required=True, help='title is required')
article_like_parser.add_argument('user_name', type=str, required=True, help='title is required')
#/////////////////////////////////////////////////////////////////

class ArticleLikeManageApi(Resource):
    def __init__(self) -> None:
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
        }
    @login_required
    def post(self):
        # check whether the user have already like the article
        # like is a mid level table for many to many relationship

        data = article_like_parser.parse_args()

        if(Likes.find_by_article_id_and_user_name(data['article_id'],data['user_name'])):
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "You have already liked this article."
            logger.warning('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{} {} {}'.format(
                request.remote_addr,request.method,request.path,404,data['user_name'],"have already liked the article with id",data['article_id']
            ))
            return make_response(jsonify(self.response_obj), 404)
        else:
            # store the like info into like table
            like = Likes()
            like.like_corr_article = data['article_id']
            like.like_corr_user = data['user_name']
            like.save()
            self.response_obj['message'] = "Article liked."
            logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{} {} {}'.format(
                request.remote_addr,request.method,request.path,200,data['user_name'],"liked the article with id",data['article_id']
            ))
            return make_response(jsonify(self.response_obj), 200)


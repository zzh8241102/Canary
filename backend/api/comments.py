from flask_restful import Resource,reqparse
from flask import jsonify, make_response,request
from numpy import array
from models import Article,User,Tags,Tags_Mid,Comments
# api for posting the article and comment
from utils.decors import login_required
from extension import logger
# //////////////////////////////////////////////////////////////////////////
article_comment_parser = reqparse.RequestParser()
article_comment_parser.add_argument('article_id', type=str, required=True, help='title is required')
# //////////////////////////////////////////////////////////////////////////
class GetCommentByArticleIdApi(Resource):
    def __init__(self) -> None:
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            'data': [],
        }
    @login_required
    def get(self):
        # get the article_id
        # get the comment info from db
        # return the comment info
    
        data = article_comment_parser.parse_args()
        
        comments = Comments.query.filter_by(comment_article=data['article_id']).all()
        if comments:
            comments_list = []
            for comment in comments:
                comment_obj = {
                    'comment_id': comment.comment_id,
                    'comment_content': comment.comment_content,
                    'comment_author': comment.comment_author,
                    'comment_time': comment.comment_time,
                    'comment_article_id': comment.comment_article,
                }
                comments_list.append(comment_obj)
            logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{}'.format(
                request.remote_addr,request.method,request.path,200,"Comments found."
            ))
            self.response_obj['message'] = "Comments found."
            self.response_obj['data'] = comments_list
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "Comments not found."
            logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{}'.format(
                request.remote_addr,request.method,request.path,404,"Comments not found."
            ))
            
            return make_response(jsonify(self.response_obj), 404)
from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from numpy import array
from models import Article, User, Tags, Tags_Mid, Comments
from utils.decors import login_required
from extension import logger
# api for posting the article and comment
# /api/post
# /api/comment

# //////////////////////////////////////////////////////////////////////
article_parser = reqparse.RequestParser()
article_parser.add_argument(
    'title', type=str, required=True, help='title is required')
article_parser.add_argument(
    'content', type=str, required=True, help='content is required')
#  tag is an array
article_parser.add_argument(
    'tags', type=str, required=True, action='append', help='tags is required')

article_parser.add_argument(
    'author', type=str, required=True, help='author is required')

# //////////////////////////////////////////////////////////////////////


class PostApi(Resource):
    def __init__(self) -> None:
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
            'data': {
                'article_id': 0,
            }
        }

    @login_required
    def post(self):
        data = article_parser.parse_args()
        #  store the article info into db
        # check whether the user is valid
        if(User.find_by_username(data['author'])):

            # we have Article model. Tag model and Tag_mid model
            # because of the many to many relationship between article and tag
            # we need to store the article and tag relation into tag_mid table
            # we need to store the article info into article table
            # we need to store the tag_mid info into tag_mid table

            # store the article info into article table
            article = Article()
            article.article_title = data['title']
            article.article_content = data['content']
            article.article_author = data['author']
            article.save()
            # # store the tag info into tag_mid table

            for i in data['tags']:
                if Tags.getTagIdbyName(i) != None:
                    tag_mid = Tags_Mid()
                    tag_mid.tag_id = Tags.getTagIdbyName(i)
                    tag_mid.article_id = article.article_id
                    tag_mid.save()

            self.response_obj['message'] = "Article posted."
            self.response_obj['data']['article_id'] = article.article_id

            logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-id:{} {}'.format(
                request.remote_addr, request.method, request.path, 200, article.article_id, "->Article posted."))
            return make_response(jsonify(self.response_obj), 200)

        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found."

            logger.warning('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{}'.format(
                request.remote_addr, request.method, request.path, 404, "User not found when posting article."))

            return make_response(jsonify(self.response_obj), 404)


# //////////////////////////////////////////////////////////////////////
Comment_parser = reqparse.RequestParser()
Comment_parser.add_argument('article_id', type=str,
                            required=True, help='article_id is required')
Comment_parser.add_argument(
    'content', type=str, required=True, help='comment is required')
Comment_parser.add_argument('commentor', type=str,
                            required=True, help='author is required')

# //////////////////////////////////////////////////////////////////////


class PostCommentApi(Resource):
    def __init__(self) -> None:
        self.response_obj = {
            'success': "true",
            'message': "",
            'code': 0,
        }

    @login_required
    def post(self):
        data = Comment_parser.parse_args()
        if(User.find_by_username(data['commentor'])):
            comment = Comments()
            comment.comment_article = data['article_id']
            comment.comment_content = data['content']
            comment.comment_author = data['commentor']
            comment.save()
            self.response_obj['message'] = "Comment posted."
            logger.info('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-id:{} {}'.format(
                request.remote_addr, request.method, request.path, 200, comment.comment_id, "->Comment posted."))
            return make_response(jsonify(self.response_obj), 200)
        else:
            self.response_obj['success'] = "false"
            self.response_obj['message'] = "User not found."
            logger.warning('[IP-Addr]-{}-[Method]-{}-[Path]-{}-[Status]-{}[Message]-{}'.format(
                request.remote_addr, request.method, request.path, 404, "User not found when posting comment."))

            return make_response(jsonify(self.response_obj), 404)

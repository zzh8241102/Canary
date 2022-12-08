#  get the article content
# the article its self with the user comments
# /api/article?article_id=article_id
from flask_restful import Resource

class ArticleContentApi(Resource):
    def get(self):
        pass
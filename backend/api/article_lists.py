# includes the all api for articles and 
# the forms shoulb be like 
# 1. /api/articleslist
# 2. /api/articleslist?tag=tagname
# 3. /api/articleslist?user=username

from flask_restful import Resource, reqparse
from flask import request,make_response
from flask import jsonify
from importlib_metadata import pass_none
from models import User


class ArticlesListApi(Resource):
    def get(self):
        pass
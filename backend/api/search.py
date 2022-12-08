# search api
# /api/search?search=keyword
# can index by tag or article name
from flask_restful import Resource

class SearchApi(Resource):
    def get(self):
        pass

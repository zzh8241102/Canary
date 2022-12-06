from flask_restful import Resource

class PostApi(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
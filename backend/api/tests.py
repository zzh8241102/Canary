from flask_restful import Resource

class TestApi(Resource):
    """
    
    /api/test

    """
    def get(self):
        return {'message': 'Hello, World!'}
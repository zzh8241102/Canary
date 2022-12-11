from flask_restful import Resource
from controller.tag_controller import generate_basic_tags

class TestApi(Resource):
    """
    
    /api/test

    """
    def get(self):
        # generate_basic_tags()
        return {'message': 'Hello, World!'}
from api import api_bp,api
from api.tests import TestApi

def add_apis():
    api.add_resource(TestApi, '/api/test')

def add_blueprints(app):
    app.register_blueprint(api_bp)
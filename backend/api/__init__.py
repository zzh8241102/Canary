from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt)

api_bp = Blueprint('api', __name__)
api = Api()

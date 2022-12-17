from email import header
from multiprocessing.spawn import import_main_path
from flask_restful import Resource, reqparse
from flask import g
from models import User
from api import api_bp
# from error_msg import forbidden
from authlib.jose import jwt
from utils.config import SECRET_KEY
import authlib.jose as jose


def generate_token(user_name):
    # a token that would not expire
    header = {'alg': 'HS256'}
    payload = {'data': user_name}
    token = jose.jwt.encode(header,payload, SECRET_KEY).decode('utf-8')
    return token

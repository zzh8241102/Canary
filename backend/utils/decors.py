# ////////////////////////////////////////
# define a decorator to check the token: employee
from hashlib import algorithms_available
from flask import make_response,request, jsonify
from functools import wraps
from models import User
from .config import SECRET_KEY
from authlib.jose import jwt, JoseError
# ////////////////////////////////////////

def login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        token_str = request.headers.get('Authorization')
        if token_str is None:
            return make_response(jsonify({'msg': 'login in is requried'}), 402)
        if token_str:
            try:
                res = jwt.decode(token_str, SECRET_KEY)
                data = res['data']
                user = User.query.filter_by(user_name=data).first()
                if user is None:
                    return make_response(jsonify({'msg': 'login in is requried'}), 402)
                else:
                    return func(self, *args, **kwargs)
            except JoseError:
                return make_response(jsonify({'msg': 'login in is requried'}), 402)
        else:
            return make_response(jsonify({'msg': 'login in is requried'}), 402)
    return wrapper


         
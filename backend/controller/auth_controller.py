import imp
from flask import g
from models import User
from api import api_bp
from error_msg import forbidden

# /// import api resources should accessed after login_required///
def login_required(func):
    def wrapper(*args, **kwargs):
        if g.user is None:
            return forbidden('Please login first')
        return func(*args, **kwargs)
    return wrapper
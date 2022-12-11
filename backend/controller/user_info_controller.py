

from flask import jsonify
from models import User

def fetch_user_info(username):
    user = User.find_by_username(username)
    # return the user info in dict
    return user
        
    
        
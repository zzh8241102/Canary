from models import Tags,Tags_Mid,User
from extension import db

def find_user_avatar_by_user_name(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    return user.user_avatar
    
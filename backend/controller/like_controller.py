from flask_restful import Resource, reqparse
from models import User,Article,Tags_Mid,Tags,Comments,Likes
from api import api_bp

def fetch_article_comment_num(article_id):
    comments = Comments.query.filter_by(comment_article=article_id).all()
    return len(comments)

def fetch_article_like_num(article_id):
    likes = Likes.query.filter_by(like_corr_article=article_id).all()
    return len(likes)


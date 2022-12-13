from flask_restful import Resource, reqparse
from flask import g
from models import User,Article,Tags_Mid,Tags
from api import api_bp

def find_article_tags(article_id):
    tags = []
    tags_mid = Tags_Mid.query.filter_by(article_id=article_id).all()
    for tag in tags_mid:
        tag_name = Tags.query.filter_by(tag_id=tag.tag_id).first()
        tags.append(tag_name.tag_name)
    return tags
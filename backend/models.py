# contains all the models and their fields
from enum import unique
from sqlalchemy import Column
from extension import db
from datetime import datetime
from passlib.apps import custom_app_context 


# ////// why bind the auth to Users model? ///////

# https://www.cnblogs.com/vovlie/p/4182814.html

# ///////////////////// end /////////////////////
class User(db.Model):
    __tablename__ = 'User'
    # user id as primary key
    user_id = db.Column(db.Integer, primary_key=True)
    # user name
    user_name = db.Column(db.String(20),nullable=False,unique=True)
    # user password using length 200 since it maybe decrpted
    user_password = db.Column(db.String(200),nullable=False)
    # user email
    user_email = db.Column(db.String(50),nullable=True)
    # user phone number
    user_phone = db.Column(db.String(20),nullable=True)
    # user
    user_reg_time = db.Column(db.DateTime, default=datetime.now)
    # user avatar url
    user_avatar = db.Column(db.String(100),nullable=True)
    # user location
    user_location = db.Column(db.String(100),nullable=True)
    
    def encrypt_password(self, password):
        self.user_password = custom_app_context.encrypt(password)
    def password_verfication(self, password):
        return custom_app_context.verify(password, self.user_password)
    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def delete(cls, user_name):
        user = cls.query.filter_by(user_name=user_name).first()
        db.session.delete(user)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(user_name = username).first()

   

class Article(db.Model):
    __tablename__ = 'Article'
    # article id as primary key
    article_id = db.Column(db.Integer, primary_key=True)
    # article title
    article_title = db.Column(db.String(100),nullable=False)
    # article content, rich format text
    article_content = db.Column(db.Text,nullable=False)
    # article author, which is a foreign key, link to user table user_id
    article_author = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    # article publish time
    published_time = db.Column(db.DateTime, default=datetime.now)
    # the author can be ref by article.author
    author = db.relationship('User', backref=db.backref('Article'))

#////////////////////////// jurstification //////////////////////////#

# why not use the more simple db.Table in many to many relation #
# because it not easy to store the extra information #
# https://stackoverflow.com/questions/45044926/db-model-vs-db-table-in-flask-sqlalchemy

#////////////////////////// jurstification end //////////////////////////#

# many to many relation
# An article can be commented by many users
# A user can comment many articles
# comments is a mid level table
class Comments(db.Model):
    # comment id as primary key
    __tablename__ = 'Comments'
    comment_id = db.Column(db.Integer, primary_key=True)
    # comment content
    comment_content = db.Column(db.Text,nullable=False)
    # comment author, which is a foreign key, link to user table user_id
    comment_author = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    # comment article, which is a foreign key, link to article table article_id
    comment_article = db.Column(db.Integer, db.ForeignKey('Article.article_id'))
    # comment time
    comment_time = db.Column(db.DateTime, default=datetime.now)
    # comment likes time
    comment_likes = db.Column(db.Integer, default=0)
    # the author can be ref by comment.author
    author = db.relationship('User', backref=db.backref('Comments'))
    # the article can be ref by comment.article
    article = db.relationship('Article', backref=db.backref('Comments'))


# many to many relation
# An article can have many tags
# A tag can be include by many articles
# tags is a mid level table
class Tags(db.Model):
    # tag id as primary key
    __tablename__ = 'Tags'
    tag_id = db.Column(db.Integer, primary_key=True)
    # tag name
    tag_name = db.Column(db.String(20),nullable=False)
    # tag description
    tag_description = db.Column(db.String(100),nullable=True)
    # tag article, which is a foreign key, link to article table article_id
    tag_corr_article = db.Column(db.Integer, db.ForeignKey('Article.article_id'))
    # the article can be ref by tag.article
    article = db.relationship('Article', backref=db.backref('Tags'))

# many to many relation
# An article can be liked by many users
# A user can like many articles
# likes is a mid level table
class Likes(db.Model):
    __tablename__ = 'Likes'
    # like id as primary key
    like_id = db.Column(db.Integer, primary_key=True)
    # like article, which is a foreign key, link to article table article_id
    like_corr_article = db.Column(db.Integer, db.ForeignKey('Article.article_id'))
    # like by whom, which is a foreign key, link to user table user_id
    like_corr_user = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    # the article can be ref by like.article
    article = db.relationship('Article', backref=db.backref('Likes'))
    # the author can be ref by like.author
    author = db.relationship('User', backref=db.backref('Likes'))

# many to many relation
# a user can have many tags
# a tag can be owned by many users
# and a tag can used to ref the article
# user_tags is a mid level table
# notice the tags must be firtly added or exist in the tags table
class UserTags(db.Model):
    # user tag id as primary key
    __tablename__ = 'UserTags'
    user_tag_id = db.Column(db.Integer, primary_key=True)
    # user tag name
    user_tag_name = db.Column(db.String(20),nullable=False)
    # user tag author, which is a foreign key, link to user table user_id
    user_tag_owner = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    # the author can be ref by user_tag.author
    author = db.relationship('User', backref=db.backref('User_tags'))
  
#tag 的入口要注意是全局唯一的
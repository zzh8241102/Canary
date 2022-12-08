# Register all the blueprints and api resources
import imp
from api import api_bp,api
from api.tests import TestApi
#  //////////////////////// gets ////////////////////////
from api.article_content import ArticleContentApi
from api.article_lists import ArticlesListApi
from api.tag_list import TagApi
from api.search import SearchApi
# //////////////////////// posts ////////////////////////
from api.posts import PostApi, PostCommentApi

from api.auth import UserRegistrationApi, UserSignInApi
# //////////////////////// api ////////////////////////
def add_apis():
    # api assembly
    api.add_resource(TestApi, '/api/test')
    api.add_resource(UserRegistrationApi, '/api/register')
    api.add_resource(UserSignInApi, '/api/signin')
    api.add_resource(ArticlesListApi, '/api/articleslist')
    api.add_resource(ArticleContentApi, '/api/article')
    api.add_resource(TagApi, '/api/tags')
    api.add_resource(PostApi, '/api/post')
    api.add_resource(PostCommentApi, '/api/comment')
    api.add_resource(SearchApi, '/api/search')
# //////////////////////// api ////////////////////////
    
# //////////////////////// blueprints ////////////////////////
def add_blueprints(app):
    app.register_blueprint(api_bp)
# //////////////////////// blueprints ////////////////////////


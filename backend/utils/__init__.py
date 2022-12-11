# Register all the blueprints and api resources

from api import api_bp,api
from api.tests import TestApi

from api.article_content import ArticleContentApi
from api.article_lists import ArticlesListApi
from api.tag_list import  TagUserApi
from api.search import SearchApi
from api.user_info import UserInfoApi
from api.user_info import ChangePasswordAPi,DeleteAccountApi

from api.posts import PostApi, PostCommentApi
from api.upload import UploadAvatarApi, FindAvatarApi
from api.user_info import ChangeUserInfoAPi

from api.auth import UserRegistrationApi, UserSignInApi
# //////////////////////// api ////////////////////////
def add_apis():
    # api assembly
    api.add_resource(TestApi, '/api/test')
    api.add_resource(UserRegistrationApi, '/api/register')
    api.add_resource(UserSignInApi, '/api/signin')
    api.add_resource(ArticlesListApi, '/api/articleslist')
    api.add_resource(ArticleContentApi, '/api/article')
    # api.add_resource(TagApi, '/api/tags')
    api.add_resource(PostApi, '/api/post')
    api.add_resource(PostCommentApi, '/api/comment')
    api.add_resource(SearchApi, '/api/search')
    api.add_resource(TagUserApi, '/api/tags')
    api.add_resource(UserInfoApi, '/api/user')
    api.add_resource(UploadAvatarApi, '/api/upload/avatar')
    api.add_resource(FindAvatarApi, '/api/find/avatar')
    api.add_resource(ChangeUserInfoAPi, '/api/user/change')
    api.add_resource(ChangePasswordAPi, '/api/user/change/password')
    api.add_resource(DeleteAccountApi, '/api/user/delete')
# //////////////////////// api ////////////////////////
    
# //////////////////////// blueprints ////////////////////////
def add_blueprints(app):
    app.register_blueprint(api_bp)
# //////////////////////// blueprints ////////////////////////


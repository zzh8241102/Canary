# Register all the blueprints and api resources

from api import api_bp,api
from api.tests import TestApi
from api.article_content import ArticleContentApi
from api.article_lists import ArticlesListApi,ArticleListByTagApi
from api.tag_list import  TagUserApi,AllTagsApi,AddNewTagApi,FindArticleTagApi, FindTaginfoByTagNameAPi,UserFollowTagApi,TagFollowerApi,UserUnfollowTagApi
from api.search import SearchApi
from api.user_info import UserInfoApi
from api.user_info import ChangePasswordAPi,DeleteAccountApi
from api.comments import GetCommentByArticleIdApi
from api.posts import PostApi, PostCommentApi
from api.upload import UploadAvatarApi, FindAvatarApi
from api.user_info import ChangeUserInfoAPi,UserActivityInfoApi,UserInfoStatsApi
from api.likes import ArticleLikeManageApi
# from api.token import TokenRefreshApi


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
    api.add_resource(PostCommentApi, '/api/postcomment')
    api.add_resource(SearchApi, '/api/search')
    api.add_resource(TagUserApi, '/api/tags')
    api.add_resource(AllTagsApi, '/api/alltags')
    api.add_resource(UserInfoApi, '/api/user')
    api.add_resource(UploadAvatarApi, '/api/upload/avatar')
    api.add_resource(FindAvatarApi, '/api/find/avatar')
    api.add_resource(ChangeUserInfoAPi, '/api/user/change')
    api.add_resource(ChangePasswordAPi, '/api/user/change/password')
    api.add_resource(DeleteAccountApi, '/api/user/delete')
    api.add_resource(AddNewTagApi, '/api/addtag')
    api.add_resource(GetCommentByArticleIdApi, '/api/comment')
    api.add_resource(ArticleLikeManageApi, '/api/like')
    api.add_resource(FindArticleTagApi, '/api/findtag')
    api.add_resource(UserActivityInfoApi, '/api/user/activity')
    api.add_resource(ArticleListByTagApi, '/api/articleslist/tag')
    api.add_resource(FindTaginfoByTagNameAPi, '/api/findtaginfo')
    api.add_resource(UserInfoStatsApi, '/api/user/stats')
    api.add_resource(UserFollowTagApi, '/api/user/followtag')
    api.add_resource(TagFollowerApi, '/api/tag/follower')
    api.add_resource(UserUnfollowTagApi, '/api/user/unfollowtag')
    # /api/refreshtoken
    
# //////////////////////// api ////////////////////////
    
# //////////////////////// blueprints ////////////////////////
def add_blueprints(app):
    app.register_blueprint(api_bp)
# //////////////////////// blueprints ////////////////////////


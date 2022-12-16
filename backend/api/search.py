# search api
# /api/search?search=keyword
# can index by tag or article name
from flask_restful import Resource,reqparse
from models import Article, Tags, User, Tags_Mid, UserTags
from flask import jsonify, make_response


# ///////////////////////////////////////////////
search_api_parser = reqparse.RequestParser()
search_api_parser.add_argument('search_content', type=str, required=True, help='search keyword is required')
# ///////////////////////////////////////////////


class SearchApi(Resource):
    def __init__(self) -> None:
        self.response_obj = {
            'article': [

            ]
        }
        
    def get(self):
        data = search_api_parser.parse_args()
        # search will back the article info like:
        # take adavantage of the aggregated search, search by tag name and article name, and article content, author, etc.
        # return the article info
        search_content = data['search_content']
        article_id_list = [] # article id list, searched article will be appended to this list
        # check the article db, return the article id list
        # search by article name, article content, article author
        article_by_name = Article.query.filter(Article.article_title.like('%'+search_content+'%')).all()
        # find the article_id and append to the article_id_list
        article_id_by_name = [item.article_id for item in article_by_name]
        article_id_list.append(article_id_by_name)
        article_by_content = Article.query.filter(Article.article_content.like('%'+search_content+'%')).all()
        article_id_by_content = [item.article_id for item in article_by_content]
        article_id_list.append(article_id_by_content)

        article_by_author = Article.query.filter(Article.article_author.like('%'+search_content+'%')).all()
        
        article_id_by_author = [item.article_id for item in article_by_author]
        article_id_list.append(article_id_by_author)

        # check the tag db, return the article id list
        # search by tag name
        tag_by_name = Tags.query.filter(Tags.tag_name.like('%'+search_content+'%')).all()
        for tag in tag_by_name:
            # use the tag_mid table to find the article id
            tag_mid = Tags_Mid.query.filter_by(tag_id=tag.tag_id).all()
            for item in tag_mid:
                article_id_list.append([item.article_id])
        # erease the duplicate list inside the article_id_list
        article_id_list = list(set([tuple(t) for t in article_id_list]))
        
        for i in article_id_list:
            for j in i:
                article = Article.query.filter_by(article_id=j).first()
                self.response_obj['article'].append({
                    'article_id': article.article_id,
                    'article_name': article.article_title,
                    'article_author': article.article_author,
                    'article_tags': [

                    ]
                })
                # find the tag name by Tags_Mid table
                tag_mid = Tags_Mid.query.filter_by(article_id=article.article_id).all()
                for item in tag_mid:
                    tag = Tags.query.filter_by(tag_id=item.tag_id).first()
                    self.response_obj['article'][-1]['article_tags'].append({
                        'tag_name': tag.tag_name
                    })
        return make_response(jsonify(self.response_obj), 200)

        
        
        






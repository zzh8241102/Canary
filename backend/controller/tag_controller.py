from models import Tags,Tags_Mid
from extension import db

def generate_basic_tags():
    

    tag_dict = {
        'Python': 'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.',
        'Flask': 'Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.',
        'llvm': 'llvm is a compiler framework for c/c++ and other languages, it is used in programming language research and development, and it is also used in many open source projects, such as clang, gcc, and so on.',
        'c++': 'c++ is a programming language which is widely used in system programming, and it is a superset of c. It is a general-purpose programming language, and it is a middle-level language, which is compiled by a compiler',
        'java': 'java is a programming language which is widely used in web backend, and it is initaily in the style of c.It uses oop to develop software, and it is widely used in the development of android applications.',
        'javascript': 'javascript is a programming language which is widely used in web frontend, and it is initaily in the style of c.It uses oop to develop software, and it is widely used in the development of android applications.',

    }
    # add the dict into db
    for key, value in tag_dict.items():
        tag = Tags(tag_name=key, tag_description=value)
        db.session.add(tag)
        db.session.commit()
 

    return True

def find_article_by_tag_name(tag_id):
    # tag and article is a many to many relation
    # tag_mid stored the relation
    # for a certain tag id, we can find all the article id
    tags_mid = Tags_Mid()
    article_id_list = tags_mid.query.filter_by(tag_id=tag_id).all()
    # convert the article id list to a list
    article_id_list = [article.article_id for article in article_id_list]
    return article_id_list


def find_article_tags(article_id):
    # tag and article is a many to many relation
    # tag_mid stored the relation
    # for a certain article id, we can find all the tag id
    tags_mid = Tags_Mid()
    tag_id_list = tags_mid.query.filter_by(article_id=article_id).all()
    # convert the tag_id lit to tag name list
    tag_name_list = [Tags.getTagNamebyId(tag.tag_id) for tag in tag_id_list]
    # convert the tag id list to a list
    return tag_name_list

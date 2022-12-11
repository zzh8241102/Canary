from models import Tags
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


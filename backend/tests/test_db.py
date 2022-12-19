from hashlib import new
import time
import unittest
import datetime
import uuid
from numpy import delete

from test_db_model import *
from werkzeug.security import check_password_hash, generate_password_hash


class UserModelTest(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()
        self.app = app
        db.create_all()

        # add some test data
        user_test_1 =  User(user_name="test1", user_password="test1", user_email="sc20zz2@leeds.ac.uk")
        user_test_1.save()
        user_test_2 =  User(user_name="test2", user_password="test2", user_email="597826725@qq.com")
        user_test_2.save()
    def test_edit_user_data(self):
        # test change email
        user_test_1 = User.find_by_username("test1")
        new_user_email = "sc20zz3@leeds.ac.uk"
        user_test_1.user_email = new_user_email
        user_test_1.user_name = "test1_new"
        user_test_1.save()
        # ////////////////////////////////////////////////////////////
        self.assertEqual(user_test_1.user_email, new_user_email)
        user_test_2 = User.find_by_username("test2")
        user_test_2.user_email = new_user_email
        user_test_2.save()
        user_test_2 = User.find_by_username("test2")
        self.assertEqual(user_test_2.user_email, new_user_email)
        # test change password
        user_test_1 = User.find_by_username("test1_new")
        new_user_password = generate_password_hash("new_password")
        user_test_1.user_password = new_user_password
        user_test_1.save()
        self.assertTrue(check_password_hash(user_test_1.user_password, "new_password"))
        user_test_2 = User.find_by_username("test2")

    def test_add_user_data(self):
        # test add new user
        user_test_3 = User(user_name="test3", user_password="test3", user_email="sc20zz2@leeds.ac.uk")
        user_test_3.save()
        user_test_3 = User.find_by_username("test3")
        self.assertEqual(user_test_3.user_name, "test3")
        self.assertEqual(user_test_3.user_email, "sc20zz2@leeds.ac.uk")
        user_test_4 = User(user_name="test4", user_password="test4", user_email="sc20zz3@leeds.ac.uk")
        user_test_4.save()
        user_test_4 = User.find_by_username("test4")
        self.assertEqual(user_test_4.user_name, "test4")
        self.assertEqual(user_test_4.user_email, "sc20zz3@leeds.ac.uk")
        user_test_5 = User(user_name="long_name", user_password="test5", user_email="sc20zz3@leeds.ac.uk")
        user_test_5.save()
        user_test_5 = User.find_by_username("long_name")
        self.assertEqual(user_test_5.user_name, "long_name")
        self.assertEqual(user_test_5.user_email, "sc20zz3@leeds.ac.uk")
    def test_delete_user_data(self):
        # create a list of new users and then delete
        user_test_6 = User(user_name="test6", user_password="test6", user_email = "sc20zz2@leeds.ac.uk")
        user_test_6.save()
        user_test_7 = User(user_name="test7", user_password="test7", user_email = "sc20zz2@leeds.ac.uk")
        user_test_7.save()
        # delete user
        user_test_6 = User.find_by_username("test6")
        user_test_6.delete()
        user_test_6 = User.find_by_username("test6")
        self.assertEqual(user_test_6, None)
        user_test_7 = User.find_by_username("test7")
        user_test_7.delete()

    def tearDown(self) -> None:

        db.session.remove()
        db.drop_all()

class ArticleModelTest(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()
        self.app = app
        db.create_all()

        # add some test data
        user_test_1 =  User(user_name="test1", user_password="test1", user_email="sc20zz2@leeds.ac.uk")
        user_test_1.save()

    def test_add_data(self):
        user_test_1 = User.find_by_username("test1")
        article_test_1 = Article(article_title="test1", article_content="test1", article_author=user_test_1.user_name)
        article_test_1.save()
        article_test_1 = Article.find_by_article_title("test1")
        self.assertEqual(article_test_1.article_title, "test1")
        self.assertEqual(article_test_1.article_content, "test1")
        self.assertEqual(article_test_1.article_author, user_test_1.user_name)
    def test_add_data_2(self):
        user_test_1 = User.find_by_username("test1")
        article_test_2 = Article(article_title="test2", article_content="test2qqdwawd", article_author=user_test_1.user_name)
        article_test_2.save()
        article_test_2 = Article.find_by_article_title("test2")
        self.assertEqual(article_test_2.article_title, "test2")
        self.assertEqual(article_test_2.article_content, "test2qqdwawd")
        self.assertEqual(article_test_2.article_author, user_test_1.user_name)
    def test_add_complex_data_3(self):
        user_test_1 = User.find_by_username("test1")
        article_test_3 = Article(article_title="test3", article_content="##|AWDWAD|QFtest2qqdwawd", article_author=user_test_1.user_name)
        article_test_3.save()
        article_test_3 = Article.find_by_article_title("test3")
        self.assertEqual(article_test_3.article_title, "test3")
        self.assertEqual(article_test_3.article_content, "##|AWDWAD|QFtest2qqdwawd")
        self.assertEqual(article_test_3.article_author, user_test_1.user_name)
    def test_edit_data(self):
        user_test_1 = User.find_by_username("test1")
        article_test_1 = Article(article_title="test1", article_content="test1", article_author=user_test_1.user_name)
        article_test_1.save()
        article_test_1 = Article.find_by_article_title("test1")
        article_test_1.article_title = "test1_new"
        article_test_1.save()
        article_test_1 = Article.find_by_article_title("test1_new")
        self.assertEqual(article_test_1.article_title, "test1_new")
        self.assertEqual(article_test_1.article_content, "test1")
        self.assertEqual(article_test_1.article_author, user_test_1.user_name)
    def test_edit_data_2(self):
        user_test_1 = User.find_by_username("test1")
        article_test_2 = Article(article_title="test2", article_content="test2qqdwawd", article_author=user_test_1.user_name)
        article_test_2.save()
        article_test_2 = Article.find_by_article_title("test2")
        article_test_2.article_title = "test2_new"
        article_test_2.save()
        article_test_2 = Article.find_by_article_title("test2_new")
        self.assertEqual(article_test_2.article_title, "test2_new")
        self.assertEqual(article_test_2.article_content, "test2qqdwawd")
        self.assertEqual(article_test_2.article_author, user_test_1.user_name)
    def test_edit_complex_data_3(self):
        user_test_1 = User.find_by_username("test1")
        article_test_3 = Article(article_title="test3", article_content="##|AWDWAD|QFtest2qqdwawd", article_author=user_test_1.user_name)
        article_test_3.save()
        article_test_3 = Article.find_by_article_title("test3")
        article_test_3.article_title = "test3_new"
        article_test_3.save()
        article_test_3 = Article.find_by_article_title("test3_new")
        self.assertEqual(article_test_3.article_title, "test3_new")
        self.assertEqual(article_test_3.article_content, "##|AWDWAD|QFtest2qqdwawd")
        self.assertEqual(article_test_3.article_author, user_test_1.user_name)
    def test_delete_data(self):
        user_test_1 = User.find_by_username("test1")
        article_test_1 = Article.find_by_article_title("test1")
        article_test_1.delete()
        article_test_1 = Article.find_by_article_title("test1")
        self.assertEqual(article_test_1, None)

class CommentSModelTest(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()
        self.app = app
        db.create_all()
        # add some test data
        comment_author =  User(user_name="test1", user_password="test1", user_email="sc20zz2@leeds.ac.uk")
        comment_author.save()
        comment = Comments(comment_content="test1", comment_author=comment_author.user_name)
    def test_add_data(self):
        comment_author = User.find_by_username("test1")
        comment_test_1 = Comments(comment_content="test1", comment_author=comment_author.user_name)
        comment_test_1.save()
        self.assertEqual(comment_test_1.comment_content, "test1")
        self.assertEqual(comment_test_1.comment_author, comment_author.user_name)
    def test_add_data_2(self):
        comment_author = User.find_by_username("test1")
        comment_test_2 = Comments(comment_content="test2", comment_author=comment_author.user_name)
        comment_test_2.save()
        self.assertEqual(comment_test_2.comment_content, "test2")
        self.assertEqual(comment_test_2.comment_author, comment_author.user_name)
    def test_add_complex_data_3(self):
        comment_author = User.find_by_username("test1")
        comment_test_3 = Comments(comment_content="##|AWDWAD|QFtest2qqdwawd", comment_author=comment_author.user_name)
        comment_test_3.save()
        self.assertEqual(comment_test_3.comment_content, "##|AWDWAD|QFtest2qqdwawd")
        self.assertEqual(comment_test_3.comment_author, comment_author.user_name)
    def test_edit_data(self):
        comment_author = User.find_by_username("test1")
        comment_test_1 = Comments(comment_content="test1", comment_author=comment_author.user_name)
        comment_test_1.save()
        comment_test_1.comment_content = "test1_new"
        comment_test_1.save()
        # find the data
        comment_test_1 = Comments.query.filter_by(comment_content="test1_new").first()
        self.assertEqual(comment_test_1.comment_content, "test1_new")
        self.assertEqual(comment_test_1.comment_author, comment_author.user_name)

    def test_edit_data_2(self):
        comment_author = User.find_by_username("test1")
        comment_test_2 = Comments(comment_content="test2", comment_author=comment_author.user_name)
        comment_test_2.save()
        comment_test_2.comment_content = "test2_new"
        comment_test_2.save()
        # find the data
        comment_test_2 = Comments.query.filter_by(comment_content="test2_new").first()
        self.assertEqual(comment_test_2.comment_content, "test2_new")
        self.assertEqual(comment_test_2.comment_author, comment_author.user_name)
    def test_edit_complex_data_3(self):
        comment_author = User.find_by_username("test1")
        comment_test_3 = Comments(comment_content="##|AWDWAD|QFtest2qqdwawd", comment_author=comment_author.user_name)
        comment_test_3.save()
        comment_test_3.comment_content = "##|AWDWAD|QFtest2qqdwawd_new"

        comment_test_3.save()
        # find the data

        comment_test_3 = Comments.query.filter_by(comment_content="##|AWDWAD|QFtest2qqdwawd_new").first()
        comment_test_3 = Comments.query.filter_by(comment_content="##|AWDWAD|QFtest2qqdwawd_new").first()
        self.assertEqual(comment_test_3.comment_author, comment_author.user_name)
    def test_delete_data(self):
        comment_test_1 = Comments.query.filter_by(comment_content="test1").first()
        db.session.delete(comment_test_1)
        db.session.commit()
        comment_test_2 = Comments.query.filter_by(comment_content="test2_new").first()
        comment_test_3 = Comments.query.filter_by(comment_content="##|AWDWAD|QFtest2qqdwawd_new").first()
        comment_test_3 = Comments.query.filter_by(comment_content="##|AWDWAD|QFtest2qqdwawd_new").first()
        comment_test_1 = Comments.query.filter_by(comment_content="test1").first()
        self.assertEqual(comment_test_1, None)
class TagsMidModelTest(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()
        self.app = app
        db.create_all()
        # add some test data
        tag_mid = Tags_Mid(tag_id=1,article_id=1)
        tag_mid.save()
    def test_add_data(self):
        tag_mid_test_1 = Tags_Mid(tag_id=2,article_id=2)
        tag_mid_test_1.save()
        self.assertEqual(tag_mid_test_1.tag_id, 2)
        self.assertEqual(tag_mid_test_1.article_id, 2)
class TestTagsModel(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()
        self.app = app
        db.create_all()
        # add some test data
        self.tag_name = "test1"+uuid.uuid4().hex[:12]
        tag = Tags(tag_name="test1",tag_description="test1")
        tag.save()
    def test_add_data(self):
        unique_tag_name = "test1"+uuid.uuid4().hex[:12]
        tag_test_1 = Tags(tag_name=unique_tag_name,tag_description="test1")
        tag_test_1.save()
        self.assertEqual(tag_test_1.tag_name, unique_tag_name)
        self.assertEqual(tag_test_1.tag_description, "test1")
    def test_edit_data(self):
        unique_tag_name = "test1"+uuid.uuid4().hex[:12]
        tag_test_1 = Tags(tag_name=unique_tag_name,tag_description="test1")
        tag_test_1.save()
        tag_test_1.tag_description = "test1_new_dec"
        tag_test_1.save()
        self.assertEqual(tag_test_1.tag_name, unique_tag_name)
    def test_delete_data(self):
        unique_tag_name = "test1"+uuid.uuid4().hex[:12]
        tag_test_1 = Tags(tag_name=unique_tag_name,tag_description="test1")
        tag_test_1.save()
        tag_test_1.tag_description = "test1_new_dec"
        tag_test_1.save()
        db.session.delete(tag_test_1)
        db.session.commit()
        tag_test_1 = Tags.query.filter_by(tag_name=self.tag_name).first()
        self.assertEqual(tag_test_1, None)
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

class TestLikeModel(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()
        self.app = app
        db.create_all()
        # add some test data
        like = Likes(like_corr_article = 1,like_corr_user=1)
        like.save()
    def test_add_data(self):
        like_test_1 = Likes(like_corr_article=2,like_corr_user=2)
        like_test_1.save()
        self.assertEqual(like_test_1.like_corr_article, 2)
        self.assertEqual(like_test_1.like_corr_user, 2)
    def test_add_data_2(self):
        like_test_2 = Likes(like_corr_article=3,like_corr_user=3)
        like_test_2.save()
        self.assertEqual(like_test_2.like_corr_article, 3)
        self.assertEqual(like_test_2.like_corr_user, 3)
    def test_add_data_3(self):
        like_test_3 = Likes(like_corr_article=4,like_corr_user=4)
        like_test_3.save()
        self.assertEqual(like_test_3.like_corr_article, 4)
        self.assertEqual(like_test_3.like_corr_user, 4)

    def test_edit_data(self):
        like_test_1 = Likes.query.filter_by(like_corr_article=2).first()
        like_test_1.like_corr_article = 100
        like_test_1.like_corr_user = 2
        like_test_1.save()
        self.assertEqual(like_test_1.like_corr_article, 100)
        self.assertEqual(like_test_1.like_corr_user, 2)
        
    def test_edit_data_2(self):
        like_test_2 = Likes.query.filter_by(like_corr_article=3).first()
        like_test_2.like_corr_article = 100
        like_test_2.like_corr_user = 3
        like_test_2.save()
        self.assertEqual(like_test_2.like_corr_article, 100)
        self.assertEqual(like_test_2.like_corr_user, 3)
    def test_edit_data_3(self):
        like_test_3 = Likes.query.filter_by(like_corr_article=4).first()
        like_test_3.like_corr_article = 100
        like_test_3.like_corr_user = 4
        like_test_3.save()
        self.assertEqual(like_test_3.like_corr_article, 100)
        self.assertEqual(like_test_3.like_corr_user, 4)
    def test_delete_data(self):
        like_test_1 = Likes(like_corr_article=313,like_corr_user=123)
        like_test_1.save()
        db.session.delete(like_test_1)
        db.session.commit()
        like_test_1 = Likes.query.filter_by(like_corr_article=313).first()
        self.assertEqual(like_test_1, None)

class TestUserTagsModel(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()
        self.app = app
        db.create_all()
        # add some test data
        user_tag = UserTags(tag_id =1 ,user_id=1)
        user_tag.save()
    def test_add_data(self):
        user_tag_test_1 = UserTags(tag_id=2,user_id=2)
        user_tag_test_1.save()
        self.assertEqual(user_tag_test_1.tag_id, 2)
        self.assertEqual(user_tag_test_1.user_id, 2)
    def test_add_data_2(self):
        user_tag_test_2 = UserTags(tag_id=3,user_id=3)
        user_tag_test_2.save()
        self.assertEqual(user_tag_test_2.tag_id, 3)
        self.assertEqual(user_tag_test_2.user_id, 3)
    def test_add_data_3(self):
        user_tag_test_3 = UserTags(tag_id=4,user_id=4)
        user_tag_test_3.save()
        self.assertEqual(user_tag_test_3.tag_id, 4)
        self.assertEqual(user_tag_test_3.user_id, 4)
    def test_edit_data(self):
        user_tag_test_1 = UserTags.query.filter_by(tag_id=2).first()
        user_tag_test_1.tag_id = 100
        user_tag_test_1.user_id = 2
        user_tag_test_1.save()
        self.assertEqual(user_tag_test_1.tag_id, 100)
        self.assertEqual(user_tag_test_1.user_id, 2)
    def test_edit_data_2(self):
        user_tag_test_2 = UserTags.query.filter_by(tag_id=3).first()
        user_tag_test_2.tag_id = 100
        user_tag_test_2.user_id = 3
        user_tag_test_2.save()
        self.assertEqual(user_tag_test_2.tag_id, 100)
        self.assertEqual(user_tag_test_2.user_id, 3)
    def test_edit_data_3(self):
        user_tag_test_3 = UserTags.query.filter_by(tag_id=4).first()
        user_tag_test_3.tag_id = 100
        user_tag_test_3.user_id = 4
        user_tag_test_3.save()
        self.assertEqual(user_tag_test_3.tag_id, 100)
        self.assertEqual(user_tag_test_3.user_id, 4)
    def test_delete_data(self):
        user_tag_test_1 = UserTags(tag_id=313,user_id=123)
        user_tag_test_1.save()
        db.session.delete(user_tag_test_1)
        db.session.commit()
        user_tag_test_1 = UserTags.query.filter_by(tag_id=313).first()
        self.assertEqual(user_tag_test_1, None)

    



if __name__ == '__main__':
    unittest.main()
    
    

        
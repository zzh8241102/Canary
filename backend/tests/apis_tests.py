


import sys
import os
from urllib import response


# ////////////////////////////////////////////////////////////////////////
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
# //////////////////////////////////////////////////////////////////////
from app import app
from extension import logger
from models import User 
import time
import json
import uuid
import unittest




# ///////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////


class LoginApiTestsClass(unittest.TestCase):
    def setUp(self):
        logger.info("Testing Login API")
        logger.info(
            '------------------------------------------------------------------')
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.token = None
            
    def test_none_exist_user(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 'adminxyz_never_reg',
                'password': 'adminxyz'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'User does not exist.')

    def test_wrong_password(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 'zzhzzh',
                'password': 'adminxyz_wrong'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'Password is wrong.')

    def test_exceess_long_password(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 'zzhzzh',
                'password': 'real_long_password_..._whcih_is_long________long'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_exceess_long_username(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 'real_long_username_..._whcih_is_long________long',
                'password': 'adminxyz'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_corner_case_username_2(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 'real_long_username_..._whcih_is_long________long',
                'password': 'adminxyz'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_corner_case_username_3(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 're',
                'password': 'adminxyz'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_corner_case_username_4(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': '123456789012345678901',
                'password': 'adminxyz'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_corner_case_username_5(self): 
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': '1234567890123456789012',
                'password': 'adminxyz'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
        
    def test_exceed_short_password(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 'real_goo',
                'password': 'admin'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_exceed_short_username(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username': 'go',
                'password': 'adminxyz'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')

    def test_success_loggin(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'true')
        self.assertEqual(res['message'], 'User signed')
        self.token = res['token']

    def test_len_corner_cases(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                '',
                'password':
                ''
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_len_corner_cases_2(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                '12',
                'password':
                '12'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_len_corner_cases_3(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                '123456789012345678901',
                'password':
                '123456789012345678901'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_len_corner_cases_4(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                '1234567890123456789012',
                'password':
                '1234567890123456789012'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_len_corner_cases_5(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                '12',
                'password':
                '12345678901234567890123'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def test_len_corner_cases_6(self):
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                '123456789012345678901',
                'password':
                '12345678901234567890123'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the user name should be between 3 and 20')
    def tearDown(self):
        logger.info('tearDown')
        logger.info('LoginApiTestsClass passed')
        logger.info(
            '------------------------------------------------------------------')

# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////# ////////////////////////////////////////////////////////////////////////# ////////////////////////////////////////////////////////////////////////# ////////////////////////////////////////////////////////////////////////


class RegApiTestClass(unittest.TestCase):
    def setUp(self):
        logger.info("Testing Reg API")
        logger.info(
            '------------------------------------------------------------------')
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.token = None

    def test_success_reg(self):
        # 拿到当前的时间戳，保留到秒
        now = str(int(time.time()))
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username': "username"+now[:16],
                'password':
                '123456',
                'email':
                "sc20zz2@leeds.ac.uk"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'true')
        self.assertEqual(res['message'], 'User created successfully.')

    def test_wrong_email(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'test',
                'password': '12345m42',
                'email':
                    '681729@ssa'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'the email format is not correct')

    def test_wrong_username(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'test____AWfnkelfD_ReaLdasAESdLLong',
                'password':
                '12313',
                'email':
                "sc20zz2@leeds.ac.uk"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Field must be between 3 and 20 characters long.')

    def test_wrong_password(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123',
                'email':
                'sc20zz2leeds.ac.uk'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Field must be between 6 and 20 characters long.')

    def test_exceed_long_password(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456789012345678901',
                'email':
                "sc20zz2@leeds.ac.uk"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Field must be between 6 and 20 characters long.')

    def test_exceed_long_username(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'test____AWfnkelfD_ReaLdasAESdLLong',
                'password':
                'adminxyz',
                'email':
                "sc20zz2@leeds.ac.uk"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Field must be between 3 and 20 characters long.')

    def test_exceed_short_password(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123',
                'email':
                "sc20zz2@leeds.ac.uk"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Field must be between 6 and 20 characters long.')

    def test_exceed_short_username(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'te',
                'password':
                'adminxyz',
                'email':
                "sc20zz2@leeds.ac.uk"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Field must be between 3 and 20 characters long.')

    def test_email_corner_case(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                'test',
                'password':
                'adminxyz',
                'email':
                "sc120zz¥leeds.ac.alsm"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'the email format is not correct')

    def test_empty_sub(self):
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username':
                '',
                'password':
                'adminxyz',
                'email':
                ""
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Field must be between 3 and 20 characters long.')
# unit test 运行入口


class EditBasicInfoApiTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # get the token for the test session
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456'
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        self.acess_token = res['token']['access_token']
        # when testing and need to acquire the resource, use the token to get the resource
        self.headers = {
            'Authorization': self.acess_token,
        }

    def test_edit_basic_info(self):
        # /api/user/change
        response = self.client.post(
            '/api/user/change',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456',
                'email':
                "sc20zz2@leeds.ac.uk",
                'phoneNumber':
                18608133373,
                'location':
                'leeds'
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)

        self.assertEqual(res['success'], 'true')

    def test_edit_basic_info_wrong_phone_num(self):
        response = self.client.post(
            '/api/user/change',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456',
                'email':
                "sc20zz2@leeds.ac.uk",
                'phoneNumber':
                186081333754,
                'location':
                'leeds'
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the phone number should be 11 digits')

    def test_edit_basic_info_wrong_email(self):
        response = self.client.post(
            '/api/user/change',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456',
                'email':
                "sc20zz2——leeds.ac.uk",
                'phoneNumber':
                18608133375,
                'location':
                'leeds'
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)

        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'the email format is not correct')

    def test_edit_basic_info_wrong_location(self):
        response = self.client.post(
            '/api/user/change',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456',
                'email':
                "sc20zz2@leeds.ac.uk",
                'phoneNumber':
                18608133375,
                'location':

                'leeds________REALLY_____LONG______LOCATION_________'
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)

        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the location should be between 3 and 20')

    def test_edit_basic_info_corner_case_location(self):
        response = self.client.post(
            '/api/user/change',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456',
                'email':
                "sc20zz2@leeds.ac.uk",
                'phoneNumber':
                18608133375,
                'location':
                '22'
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)

        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the location should be between 3 and 20')

    def tearDown(self):
        pass


class ResetPasswordApiTest(unittest.TestCase):
    # notice here, the password will be reset to a more complex one after the test
    def setUp(self):
        # sign in to get the token
        self.client = app.test_client()
        now = str(int(time.time()))
        # uuid 生成唯一的id,10位长
        self.username = 'test' + str(uuid.uuid4())[:13]
        
        
        
        response = self.client.post(
            '/api/register',
            data=json.dumps({
                'username': self.username,
                'password':
                '123456',
                'email':
                "sc20zz2@leeds.ac.uk"
            }),
            content_type='application/json'
        )
        res = json.loads(response.data)
        
        
        self.acess_token = res['token']['access_token']
        self.headers = {
            'Authorization': self.acess_token,
        }
        
        

    def test_wrong_old_password(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '1234567aedaefaefdaewdawdddsa____Eadknwaow++',
                'newPassword':
                '1234567zzhadmin'
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_wrong_new_password(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '123456',
                'newPassword':
                '1234567zzhadmin___W_AWDAWDDWAW___AWF_D_AWDAWD___WAD'
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_corner_case_new_password(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '123456',
                'newPassword':
                ''
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_corner_case_new_password_2(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '123456',
                'newPassword':
                '123456789012345678901'
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_corner_case_new_password_3(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '123456',
                'newPassword':
                '12345678901234567890122'
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_corner_case_old_password(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '',
                'newPassword':
                '123456789012345678901'
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_corner_case_old_password_2(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '123456789012345678901',
                'newPassword':
                '123456789012345678901'
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')

    def test_corner_case_old_password_3(self):
        response = self.client.post(
            '/api/user/change/password',
            data=json.dumps({
                'username':
                self.username,
                'oldPassword':
                '1234567890123456789012',
                'newPassword':
                '1234567890123456789012'
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'the length of the password should be between 6 and 20')


class PostNewCommentTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # login to the username test and password 123456 to get the token
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456'
            }), content_type='application/json'
        )
        self.username = 'test'
        res = json.loads(response.data)
        

        self.access_token = res['token']['access_token']

        self.headers = {
            'Authorization': self.access_token,
        }

    def test_post_new_comment(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                 1,
                'content':
                'this is a test comment for unit test',
                'commentor':
                self.username
            }), content_type='application/json',
            headers=self.headers
        )
        
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'true')
        self.assertEqual(res['message'], 'Comment posted.')

    def test_post_new_comment_2(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                 1,
                'content':
                'this is a test comment for unit test as well',
                'commentor':
                self.username
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'true')
        self.assertEqual(res['message'], 'Comment posted.')

    def test_post_new_comment_3_wrong_empty(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                 1,
                'content':
                '',
                'commentor':
                self.username
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'Invalid input.')
    def test_post_new_comment_4_wrong_empty(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                 1,
                'content':
                'this is a test comment for unit test as well',
                'commentor':
                ''
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'Invalid input.')
    def test_wrong_commentor_corner_case(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    1,
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "123456789012345678901"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_commentor_corner_case_2(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    1,
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "1234567890123456789012"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_commentor_corner_case_3(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    1,
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "12345678901234567890123"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_article_info(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    "22",
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "12345678901234567890123"
            }), content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_article_info_2(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    "22131",
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "12345678901234567890123"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_article_info_and_wrong_commentor(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    "22131",
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "123456789012345678901234"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_article_info_and_wrong_commentor_2(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    "22131",
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "1234567890123456789012345"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false') 
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_article_info_and_wrong_commentor_3(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    "22131",
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "12345678901234567890123456"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
    def test_wrong_article_info_and_wrong_commentor_4(self):
        response = self.client.post(
            '/api/postcomment',
            data=json.dumps({
                'article_id':
                    "22131",
                'content':
                    'this is a test comment for unit test as well',
                'commentor':
                "123456789012345678901234567"
            }), content_type='application/json',
            headers=self.headers
        )

        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(
            res['message'], 'Invalid input.')
class AddNewTagApiTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # login to the username test and password 123456 to get the token
        response = self.client.post(
            '/api/signin',
            data=json.dumps({
                'username':
                'test',
                'password':
                '123456'
            }), content_type='application/json'
        )
        self.username = 'test'
        res = json.loads(response.data)
        

        self.access_token = res['token']['access_token']

        self.headers = {
            'Authorization': self.access_token,
        }
            
    def test_add_new_tag(self):
        rand_back = str(uuid.uuid4())[:10]
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                    'foo_bar'+rand_back,
                'tag_description':
                    'this is a test tag for unit test ',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'true')
        self.assertEqual(res['message'], 'successfully add the tag')
    def test_add_existing_tag(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                    'foo_bar',
                'tag_description':
                    'this is a test tag for unit test ',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'tag already exist')
    def test_add_new_tag_with_wrong_name_length(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                '',
                'tag_description':
                'this is a test tag for unit test ',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'invalid input for tag name')

    def test_add_new_tag_with_wrong_name_length_2(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                '1',
                'tag_description':
                'this is a test tag for unit test ',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'invalid input for tag name')
    def test_add_new_tag_with_wrong_name_length_3(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                '12',
                'tag_description':
                'this is a test tag for unit test ',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'invalid input for tag name')

    def test_add_new_tag_wrong_description(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                'foo_bar',
                'tag_description':
                '',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'invalid input for tag description')
    def test_add_new_tag_wrong_description_2(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                'foo_bar',
                'tag_description':
                '1',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'invalid input for tag description')
    def test_add_new_tag_wrong_description_3(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                'foo_bar',
                'tag_description':
                '12',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'invalid input for tag description')
    def test_add_new_tag_wrong_description_4(self):
        response = self.client.post(
            '/api/addtag',
            data=json.dumps({
                'tag_name':
                'foo_bar',
                'tag_description':
                'x',
            }),
            content_type='application/json',
            headers=self.headers
        )
        res = json.loads(response.data)
        self.assertEqual(res['success'], 'false')
        self.assertEqual(res['message'], 'invalid input for tag description')

if __name__ == '__main__':

    unittest.main()

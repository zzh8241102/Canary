
import sys
import os

# 时间戳
import time

# ///////////////////////////////////////////////////////////////////////
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
# ////////////////////////////////////////////////////////////////////////

import json
from app import app
from models import User
from extension import logger
import unittest

# ////////////////////////////////////////////////////////////////////////
class LoginApiTestsClass(unittest.TestCase):
    def setUp(self):
        logger.info("Testing Login API")
        logger.info('------------------------------------------------------------------')
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

    def tearDown(self):
        logger.info('tearDown')
        logger.info('LoginApiTestsClass passed')
        logger.info('------------------------------------------------------------------')

# ////////////////////////////////////////////////////////////////////////
class RegApiTestClass(unittest.TestCase):
    def setUp(self):
        logger.info("Testing Reg API")
        logger.info('------------------------------------------------------------------')
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
            data = json.dumps({
                'username':"username"+now[:16],
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
                'password':'12345m42',
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
        self.assertEqual(res['message'], 'Field must be between 3 and 20 characters long.')
    
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
        self.assertEqual(res['message'], 'Field must be between 6 and 20 characters long.')


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
        self.assertEqual(res['message'], 'Field must be between 3 and 20 characters long.')
# unit test 运行入口
if __name__ == '__main__':
    unittest.main()

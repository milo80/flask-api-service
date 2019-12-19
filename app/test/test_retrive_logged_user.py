from app.test.base import BaseTestCase
from app.main.service.auth_service import Auth
from flask import request

import json


def register_user(self):
    return self.client.post(
        '/api/users',
        data=json.dumps(dict(
            email='example@gmail.com',
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='example@gmail.com',
            password='123456'
        )),
        content_type='application/json'
    )


class TestRetriveUser(BaseTestCase):

    def test_getting_logged_in_user(self):
        """Test for retriving logged in user"""
        with self.client:
            # user registration
            user_response = register_user(self)
            # log in user
            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])

            # response request header
            # user logged in retrive
            print('---------------><----------------')
            print(request.headers.get('Authorization'))
            data, status = Auth.get_logged_in_user()
            print('data {}',data)
            print(status)
            user_details = Auth.get_logged_in_user(data)
            # user_data = json.loads(user_details)
            if user_details:
                print('////// ---- //////')
                print(type(user_details))
                print(user_details)
                print('////// ---- //////')
            else:
                print('////// ---- //////')
                print('something wrong')
                print('////// ---- //////')


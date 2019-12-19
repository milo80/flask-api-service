from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'email': fields.String(required=True, description='email addresss'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='the email register requirement'),
        'password': fields.String(required=True, description='the user password')
    })

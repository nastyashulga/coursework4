import hashlib
from datetime import datetime, timedelta

from jwt import jwt

from constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class AuthService():
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def auth_user(self, email, password):
        user = self.dao.get_by_username(email)

        if not user:
            return None

        hash_password = self.get_hash(password)

        if hash_password != user.password:
            return None

        data = {
            'email': user.username,
        }

        return self.get_access_token(data)

    def get_hash(self, password: str):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode('utf-8', 'ignore')

    def get_access_token(self, data: dict):
        min10 = datetime.utcnow() + timedelta(days=10)
        data['exp'] = int(min10.timestamp())
        access_token = jwt.encode(data, PWD_HASH_SALT)

        days130 = datetime.utcnow() + timedelta(days=130)
        data['exp'] = int(days130.timestamp())
        refresh_token = jwt.encode(data, PWD_HASH_SALT)

        return {'access_token': access_token, 'refresh_token': refresh_token}


    def check_refresh_token(self, refresh_token):
        try:
            data = jwt.decode(jwt=refresh_token, key=PWD_HASH_SALT, algorithms='HS256')
        except Exception as e:
            return None

        tokens = self.get_access_token(data)

        return tokens

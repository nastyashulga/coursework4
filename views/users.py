import hashlib

from flask import request
from flask_restx import Resource, Namespace

from constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.model.user import UserSchema
from implemented import user_service

users_ns = Namespace('users')


@users_ns.route('/')
class UserView(Resource):
    def get(self):
        users = user_service.get_all()
        result = UserSchema(many=True).dump(users)
        return result, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201


@users_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)
        return result, 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204

    def get_hash(password: str):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode('utf-8', 'ignore')

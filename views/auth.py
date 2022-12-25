from flask import request
from flask_restx import Resource, Namespace, abort

from constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.model.user import UserSchema
from implemented import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        data = request.json

        if not data.get('email') or not data.get('password'):
            abort(400)

        user_service.create(data)

        return "", 201

@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        req_json = request.json

        email = req_json.get('email')
        password = req_json.get('password')

        if not email and password:
            abort(400)

        token = auth_service.auth_user(email, password)

        if not token:
            return {"error": "Ошибка в логине или пароле"}, 401

        return token, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')

        if refresh_token is None:
            abort(400)

        tokens = auth_service.check_refresh_token(refresh_token)

        return tokens, 201



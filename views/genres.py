from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from utils import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        res = genre_service.get_all()
        return res, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_item_by_id(gid)
        return genre, 200


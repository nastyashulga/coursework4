from flask import request
from flask_restx import Resource, Namespace, abort


from implemented import movie_service
from utils import auth_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        data = {
            'status' : request.args.get('satus'),
            'page' : request.args.get('page')
        }
        movies = movie_service.get_all_movies(data)
        return movies, 200


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_item_by_id(mid)

        if not movie:
            abort(404,message='Movie not found')

        return movie, 200





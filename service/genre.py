from dao.genre import GenreDAO
from dao.model.genre import GenreSchema

class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_item_by_id(self, gid):
        genre = self.dao.get_by_id(gid)
        return GenreSchema().dump(genre)

    def get_all(self):
        genres = self.dao.get_all()
        return GenreSchema(many=True).dump(genres)


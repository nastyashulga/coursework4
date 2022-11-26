from setup_db import db
from dao.model.basemodel import BaseModelId
from marshmallow import Schema, fields


class User(BaseModelId, db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()


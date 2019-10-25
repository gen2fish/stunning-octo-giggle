from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy



ma = Marshmallow()
db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    format = db.Column(db.String(250), nullable=False)
    releaseYear = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    creationDate = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, movie):
        self.movie = movie

class MovieSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    format = fields.String()
    releaseYear = fields.Integer()
    rating = fields.Integer()
    creation_date = fields.DateTime()

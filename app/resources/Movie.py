from flask import request
from flask_restful import Resource
from model import db, Movie, MovieSchema
import logging

movie_schema = MovieSchema()

class movieResource(Resource):
  def get(self):
    movies = Movie.query.all()
    logging.basicConfig(level=logging.DEBUG)
    movies_json = []
    for mov in movies:
      movies_json.append(movie_schema.dump(mov))

    return {'status': 'sucess', 'data': movies_json}, 200

  def post(self):
    json_data = request.get_json(force=True)
    if not json_data:
      return {'message': 'No valid JSON provided'}, 400
    # Validate
    fields = ['title', 'format', 'rating', 'releaseYear']
    data = movie_schema.load(json_data)

    movie = Movie.query.filter_by(title=data['title']).first()
    if movie:
      return {'message': 'Title already exists'}, 400

    movie = Movie(
      title = json_data['title'],
      format = json_data['format'],
      rating = json_data['rating'],
      releaseYear = json_data['releaseYear']
    )

    db.session.add(movie)
    db.session.commit()

    result = movie_schema.dump(movie)
    return { 'status': 'successful', 'data': result }, 201

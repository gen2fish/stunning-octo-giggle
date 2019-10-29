from flask import request
from flask_restful import Resource
from model import db, Movie, MovieSchema
import logging

movie_schema = MovieSchema()
logging.basicConfig(level=logging.DEBUG)

class movieAllResource(Resource):
  def get(self):
    # Query DB
    movies = Movie.query.all()

    # Format and Return
    if movies:
      movies_json = []
      for movie in movies:
        movies_json.append(movie_schema.dump(movie))
      return {'status': 'sucess', 'data': movies_json}, 200
    else:
      return {'message': 'error', 'data': 'No movies found'}, 404

  def post(self):
    # JSON-ify
    json_data = request.get_json(force=True)
    if not json_data:
      return {'message': 'No valid JSON provided'}, 400
    data = movie_schema.load(json_data)

    # Validate new record is unique by title
    movie = Movie.query.filter_by(title=data['title']).first()
    if movie:
      return {'message': 'Title already exists'}, 400

    # Parse and Commit
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

class movieResource(Resource):
  def get(self, mid):
    # Get the record and parse
    movies = Movie.query.filter_by(id=mid).first()
    if movies:
      movies_json = (movie_schema.dump(movies))
      return {'status': 'sucess', 'data': movies_json}, 200
    else:
      return {'message': 'error', 'data': 'Movie not found'}, 404

  def put(self, mid):
    # Get JSON and see if Record can be found
    json_data = request.get_json(force=True)
    if not json_data:
      return {'message': 'No valid JSON provided'}, 400
    data = movie_schema.load(json_data)

    # See if the new title already exists
    movie = Movie.query.filter_by(title=data['title']).first()
    if movie:
      return {'message': 'Title already exists'}, 400

    # All good! Put it in and return
    movie = Movie.query.filter_by(id=mid).first()
    if movie:
      movie.title = data['title']
      movie.rating = data['rating']
      movie.format = data['format']
      movie.releaseYear = data['releaseYear']
      db.session.commit()

      result = movie_schema.dump(movie)
      return { 'status': 'successful', 'data': result }, 201
    else:
      return { 'status': 'error', 'data': 'Movie not found'}, 404

  def delete(self, mid):
    # Find the thing
    movies = Movie.query.filter_by(id=mid).first()
    if movies:
      logging.debug(movies)
      # Delete the thing
      movies = Movie.query.filter_by(id=mid).delete()
      db.session.commit()
      result = movie_schema.dump(movies)
      return {'status': 'success'}, 204
    else:
      return {'message': 'error', 'data': 'Movie not found'}, 404

from flask import request
from flask_restful import Resource
from model import db, Movie, MovieSchema

movie_schema = MovieSchema()

class movieResource(Resource):
  def get(self):
    movies = Movie.query.all()
    movies = movie_schema.dump(movies)
    return {'status': 'sucess', 'data': movies}, 200

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

    result = movie_schema.dump(movie).data
    return { 'status': 'successful', 'data': result }, 201

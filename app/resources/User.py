from flask import request
from flask_restful import Resource
from model import db, User, UserSchema
from flask_httpauth import HTTPBasicAuth
import logging

user_schema = UserSchema()
logging.basicConfig(level=logging.DEBUG)
auth = HTTPBasicAuth()


class userAllAuth(Resource):
  def post(self):
    logging.debug("Test")
    json_data = request.get_json(force=True)
    if not json_data:
      return {'message': 'No valid JSON provided'}, 400

    if json_data['username'] is None or json_data['password'] is None:
      return {'message': 'Missing Arguments'}, 400 # missing arguments
    user = User.query.filter_by(username=json_data['username']).first()
    if user:
      return {'message': 'User Exists'}, 400 # missing arguments

    userpost = User(username = json_data['username'])
    userpost.hash_password(json_data['password'])
    db.session.add(userpost)
    db.session.commit()
    return {'message': 'Username created successfully'}, 201

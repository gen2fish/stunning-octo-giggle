from flask import Blueprint
from flask_restful import Api
from resources.User import userAllAuth
from resources.Movie import movieResource, movieAllResource
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(movieAllResource, '/movie')
api.add_resource(movieResource, '/movie/<int:mid>')
api.add_resource(userAllAuth, '/user')
# api.add_resource(userAuth, '/user/<int:uid>')

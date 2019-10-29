from flask import Blueprint
from flask_restful import Api
from resources.Movie import movieResource, movieAllResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(movieAllResource, '/Movie')
api.add_resource(movieResource, '/Movie/<int:mid>')

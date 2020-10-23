from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.adapters.gcloudrepository import GCloudRepository
from backendflask.domain_models.genre import Genre
import json

# DB Connection
db = MemoryRepository()
#db = GCloudRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('genreName', type=str,
                    help="Name of the genre")


class GenreList(Resource):
    def get(self):
        response = {
            "genres":  [genre.toJSON() for genre in db.get_all_genres()]
        }
        return make_response(jsonify(response), 200)

    def post(self):
        args = parser.parse_args()
        response = {
            "successful": False,
            "genreName": args['genreName'],
        }
        response['successful'] = True if db.add_genre(
            Genre(
                genre_name=args['genreName'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.domain_models.genre import Genre

# DB Connection
db = MemoryRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('genreName', type=str,
                    help="Name of the genre")


class GenreList(Resource):
    def get(self):
        response = {
            "genres":  db.get_all_genres()
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


class Genre(Resource):
    def get(self, genreID: str) -> str:
        genre = db.get_genre(genreID=genreID)
        response = {
            "successful": True if genre else False,
            "genre": genre,
        }
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

    def put(self, genreID: str) -> str:
        args = parser.parse_args()
        response = {
            "successful": False,
            "genreName": args['genreName'],
        }
        response['successful'] = True if db.update_genre(
            Genre(
                genreID=genreID,
                genre_name=args['genreName'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

    def delete(self, genreID: str) -> str:
        response = {
            "successful": False,
        }
        response['successful'] = True if db.delete_genre(
            genreID=genreID) else False
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

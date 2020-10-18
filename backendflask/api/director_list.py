from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.adapters.gcloudrepository import GCloudRepository
from backendflask.domain_models.director import Director
import json

# DB Connection
db = MemoryRepository()
#db = GCloudRepository()


# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('personID', type=str,
                    help="Person Identifier")
parser.add_argument('fullName', type=str,
                    help="Persons full name")
parser.add_argument('gender', type=int,
                    help="Persons gender")
parser.add_argument('dateOfBirth', type=str,
                    help="Persons date of birth")
parser.add_argument('imdbPage', type=str,
                    help="Persons IMDB page")


class DirectorList(Resource):
    def get(self):
        response = {
            "directors": [director.toJSON() for director in db.get_all_directors()]
        }
        return make_response(jsonify(response), 200)

    def post(self):
        args = parser.parse_args()
        response = {
            "successful": False,
            "fullName": args['fullName'],
            "gender": args['gender'],
            "dateOfBirth": args['dateOfBirth'],
            "imdbPage": args['imdbPage'],
        }
        response['successful'] = True if db.add_director(
            Director(
                full_name=args['fullName'],
                gender=args['gender'],
                date_of_birth=args['dateOfBirth'],
                imdb_page=args['imdbPage'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.domain_models.rating import Rating
from backendflask.domain_models.movie import Movie
import json

# DB Connection
db = MemoryRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('ratingID', type=str,
                    help="Rating Identifier")
parser.add_argument('personID', type=str,
                    help="User ID of the user who posted the rating")
parser.add_argument('movieTitle', type=str,
                    help="Title of the movie being rated")
parser.add_argument('rating', type=float,
                    help="Rating from 1 to 10")


class RatingList(Resource):
    def get(self):
        response = {
            "ratings":  [rating.toJSON() for rating in db.get_all_ratings()]
        }
        return make_response(jsonify(response), 200)

    def post(self):
        args = parser.parse_args()
        response = {
            "successful": False,
            "personID": args['personID'],
            "movieTitle": args['movieTitle'],
            "rating": args['rating']
        }
        response['successful'] = True if db.add_rating(
            Rating(
                personID=args['personID'],
                movie=Movie(title=args['movieTitle']),
                rating=args['rating'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

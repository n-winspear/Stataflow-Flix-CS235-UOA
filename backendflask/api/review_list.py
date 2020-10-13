from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.domain_models.review import Review
from backendflask.domain_models.movie import Movie
import json

# DB Connection
db = MemoryRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('reviewID',
                    help="Review Identifier")
parser.add_argument('personID',
                    help="User ID of the user who posted the review")
parser.add_argument('movieTitle',
                    help="Title of the movie being reviewed")
parser.add_argument('reviewText',
                    help="Text content of the review posted")


class ReviewList(Resource):

    def get(self):
        response = {
            "reviews":  [review.toJSON() for review in db.get_all_reviews()]
        }
        return make_response(jsonify(response), 200)

    def post(self):
        args = parser.parse_args()
        response = {
            "successful": False,
            "personID": args['personID'],
            "movieTitle": args['movieTitle'],
            "reviewText": args['reviewText']
        }
        response['successful'] = True if db.add_review(
            Review(
                reviewID=args['reviewID'],
                personID=args['personID'],
                movie=Movie(title=args['movieTitle']),
                review_text=args['reviewText'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

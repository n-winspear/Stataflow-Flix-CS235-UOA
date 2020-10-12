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

parser.add_argument('reviewID', type=str,
                    help="Review Identifier")
parser.add_argument('userID', type=str,
                    help="User ID of the user who posted the review")
parser.add_argument('movieTitle', type=str,
                    help="Title of the movie being reviewed")
parser.add_argument('reviewText', type=str,
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
            "userID": args['userID'],
            "movie": args['movieTitle'],
            "reviewText": args['reviewText']
        }
        response['successful'] = True if db.add_review(
            Review(
                userID=args['userID'],
                movie=Movie(title=args['movieTitle']),
                review_text=args['reviewText'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)


class Review(Resource):
    def get(self, reviewID: str) -> str:
        review = db.get_review(reviewID=reviewID)
        response = {
            "successful": True if review else False,
            "review": review.toJSON(),
        }
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

    def put(self, reviewID: str) -> str:
        args = parser.parse_args()
        response = {
            "successful": False,
            "userID": args['userID'],
            "movie": args['movieTitle'],
            "reviewText": args['reviewText']
        }
        response['successful'] = True if db.update_review(
            Review(
                reviewID=reviewID,
                userID=args['userID'],
                movie=Movie(title=args['movieTitle']),
                review_text=args['reviewText'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

    def delete(self, reviewID: str) -> str:
        response = {
            "successful": False,
        }
        response['successful'] = True if db.delete_review(
            reviewID=reviewID) else False
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

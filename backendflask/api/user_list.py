from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.domain_models.user import User
from backendflask.domain_models.movie import Movie
from backendflask.domain_models.review import Review
import json

# DB Connection
db = MemoryRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('personID')
parser.add_argument('firstName')
parser.add_argument('lastName')
parser.add_argument('gender')
parser.add_argument('emailAddress')
parser.add_argument('password')
parser.add_argument('phoneNumber')
parser.add_argument('watchlist')
parser.add_argument('watchedMovies')
parser.add_argument('reviews')


class UserList(Resource):

    def get(self):
        response = {
            "reviews":  [user.toJSON() for user in db.get_all_users()]
        }
        return make_response(jsonify(response), 200)

    def post(self):
        args = parser.parse_args()
        response = {
            "successful": False,
            "personID": args['personID'],
            "firstName": args['firstName'],
            "lastName": args['lastName'],
            "gender": args['gender'],
            "emailAddress": args['emailAddress'],
            "password": args['password'],
            "phoneNumber": args['phoneNumber'],
            "watchlist": args['watchlist'],
            "watchedMovies": args['watchedMovies'],
            "reviews": args['reviews'],
        }
        response['successful'] = True if db.add_review(
            User(
                personID=args['personID'],
                firstName=args['firstName'],
                lastName=args['lastName'],
                gender=args['gender'],
                emailAddress=args['emailAddress'],
                password=args['password'],
                phoneNumber=args['phoneNumber'],
                watchlist=[Movie(title=movie.movieTitle)
                           for movie in args['watchlist']],
                watchedMovies=[Movie(title=movie.movieTitle)
                               for movie in args['watchedMovies']],
                reviews=args['reviews'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

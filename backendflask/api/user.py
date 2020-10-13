from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.domain_models.user import User
from backendflask.domain_models.movie import Movie
from backendflask.domain_models.user import User
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
parser.add_argument('users')


class User(Resource):
    def get(self, personID: str) -> str:
        user = db.get_user(personID=personID)
        response = {
            "successful": True if user else False,
            "user": user.toJSON(),
        }
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

    def put(self, personID: str) -> str:
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
        response['successful'] = True if db.update_user(
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

    def delete(self, personID: str) -> str:
        response = {
            "successful": False,
        }
        print(personID, db)
        response['successful'] = True if db.delete_user(
            personID=personID) else False
        print(response['successful'])
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

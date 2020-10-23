from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from adapters.memoryrepository import MemoryRepository
from adapters.gcloudrepository import GCloudRepository
from domain_models.user import User
from domain_models.movie import Movie
from domain_models.review import Review
import json

# DB Connection
db = MemoryRepository()
#db = GCloudRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('personID')
parser.add_argument('firstName')
parser.add_argument('lastName')
parser.add_argument('gender')
parser.add_argument('emailAddress')
parser.add_argument('password')
parser.add_argument('phoneNumber')
parser.add_argument('dateOfBirth')
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
            "personID": args['personID'] if args['personID'] else None,
            "firstName": args['firstName'] if args['firstName'] else None,
            "lastName": args['lastName'] if args['lastName'] else None,
            "gender": args['gender'] if args['gender'] else None,
            "emailAddress": args['emailAddress'] if args['emailAddress'] else None,
            "password": args['password'] if args['password'] else None,
            "phoneNumber": args['phoneNumber'] if args['phoneNumber'] else None,
            "dateOfBirth": args['dateOfBirth'] if args['dateOfBirth'] else None,
            "watchlist": args['watchlist'] if args['watchlist'] else None,
            "watchedMovies": args['watchedMovies'] if args['watchedMovies'] else None,
            "reviews": args['reviews'] if args['reviews'] else None,
        }
        response['successful'] = True if db.add_user(
            User(
                personID=args['personID'] if args['personID'] else None,
                first_name=args['firstName'] if args['firstName'] else None,
                last_name=args['lastName'] if args['lastName'] else None,
                gender=args['gender'] if args['gender'] else None,
                email_address=args['emailAddress'] if args['emailAddress'] else None,
                password=args['password'] if args['password'] else None,
                phone_number=args['phoneNumber'] if args['phoneNumber'] else None,
                date_of_birth=args['dateOfBirth'] if args['dateOfBirth'] else None,
                watchlist=[Movie(title=movie.movieTitle)
                           for movie in args['watchlist']] if args['watchlist'] else [],
                watched_movies=[Movie(title=movie.movieTitle)
                                for movie in args['watchedMovies']] if args['watchedMovies'] else [],
                reviews=[Review(personID=review.personID, movie=review.movieTitle, review_text=review.reviewText)
                         for review in args['reviews']] if args['reviews'] else [],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

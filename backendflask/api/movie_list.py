from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.domain_models.movie import Movie
from backendflask.domain_models.actor import Actor
from backendflask.domain_models.director import Director
from backendflask.domain_models.genre import Genre
import json

# DB Connection
db = MemoryRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('movieID', type=str,
                    help="Movie Identifier")
parser.add_argument('movieTitle', type=str,
                    help="Title of the movie")
parser.add_argument('releaseYear', type=int,
                    help="Release year of movie")
parser.add_argument('genres', type=list,
                    help="List of movie genres")
parser.add_argument('description', type=str,
                    help="Movie description")
parser.add_argument('directors', type=list,
                    help="List of movie directors")
parser.add_argument('actors', type=list,
                    help="List of movie actors")
parser.add_argument('runtimeMinutes', type=int,
                    help="Movie runtime in minutes")
parser.add_argument('averageRating', type=float,
                    help="Average of movie ratings")
parser.add_argument('voteCount', type=int,
                    help="Number of ratings submitted")
parser.add_argument('revenue', type=float,
                    help="Revenue generated by the movie")
parser.add_argument('metascore', type=float,
                    help="Movie metascore")


class MovieList(Resource):
    def get(self):
        response = {
            "movies":  [movie.toJSON() for movie in db.get_all_movies()]
        }
        return make_response(jsonify(response), 200)

    def post(self):
        args = parser.parse_args()
        response = {
            "successful": False,
            "movieID": args['movieID'],
            'movieTitle': args['movieTitle'],
            'releaseYear': args['releaseYear'],
            'genres': args['genres'],
            'description': args['description'],
            'directors': args['directors'],
            'actors': args['actors'],
            'runtimeMinutes': args['runtimeMinutes'],
            'averageRating': args['averageRating'],
            'voteCount': args['voteCount'],
            'revenue': args['revenue'],
            'metascore': args['metascore'],
        }
        response['successful'] = True if db.add_movie(
            Movie(
                title=args['movieTitle'],
                release_year=args['releaseYear'],
                genres=[Genre(
                    genre_name=genre
                ) for genre in args['genres']],
                description=args['description'],
                directors=[Director(
                    full_name=director['fullName'],
                    gender=director['gender'],
                    date_of_birth=director['dateOfBirth'],
                    imdb_page=director['imdbPage'],
                ) for director in args['directors']],
                actors=[Actor(
                    full_name=actor['fullName'],
                    gender=actor['gender'],
                    date_of_birth=actor['dateOfBirth'],
                    imdb_page=actor['imdbPage'],
                ) for actor in args['actors']],
                runtime_minutes=args['runtimeMinutes'],
                average_rating=args['averageRating'],
                vote_count=args['voteCount'],
                revenue=args['revenue'],
                metascore=args['metascore'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)
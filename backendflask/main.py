#!flask/bin/python
from flask import Flask, jsonify, make_response, request
from flask_restful import Api
from flask_cors import CORS, logging
from backendflask.api.review import Review
from backendflask.api.rating import Rating
from backendflask.api.movie import Movie
from backendflask.api.genre import Genre
from backendflask.api.director import Director
from backendflask.api.actor import Actor
from backendflask.api.user import User
from backendflask.api.review_list import ReviewList
from backendflask.api.rating_list import RatingList
from backendflask.api.movie_list import MovieList
from backendflask.api.genre_list import GenreList
from backendflask.api.director_list import DirectorList
from backendflask.api.actor_list import ActorList
from backendflask.api.user_list import UserList
from uuid import uuid4

# API URL
API_VERSION = 1
API_BASE_URL = f"/v{API_VERSION}"

# Globals
app = Flask(__name__)
api = Api(app)
cors = CORS(app)

logging.getLogger('flask_cors').level = logging.DEBUG

# Error Handler


@ app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# API Resources

# Actors
api.add_resource(ActorList, f"{API_BASE_URL}/actors")
api.add_resource(
    Actor, f"{API_BASE_URL}/actors/<string:personID>")

# Directors
api.add_resource(DirectorList, f"{API_BASE_URL}/directors")
api.add_resource(
    Director, f"{API_BASE_URL}/directors/<string:personID>")

# Genres
api.add_resource(GenreList, f"{API_BASE_URL}/genres")
api.add_resource(
    Genre, f"{API_BASE_URL}/genres/<string:genreID>")

# Movies
api.add_resource(MovieList, f"{API_BASE_URL}/movies")
api.add_resource(
    Movie, f"{API_BASE_URL}/movies/<string:movieID>")

# Ratings
api.add_resource(RatingList, f"{API_BASE_URL}/ratings")
api.add_resource(
    Rating, f"{API_BASE_URL}/ratings/<string:ratingID>")

# Reviews
api.add_resource(ReviewList, f"{API_BASE_URL}/reviews")
api.add_resource(
    Review, f"{API_BASE_URL}/reviews/<string:reviewID>")

# Users
api.add_resource(UserList, f"{API_BASE_URL}/users")
api.add_resource(
    User, f"{API_BASE_URL}/user/<string:emailAddress>")


# App Runner
if __name__ == '__main__':
    app.run(debug=True)

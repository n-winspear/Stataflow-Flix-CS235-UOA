#!flask/bin/python
from flask import Flask, jsonify, make_response, request
from flask_restful import Api
from flask_cors import CORS
from api.reviews import ReviewList, Review
from api.ratings import RatingList, Rating
from api.movies import MovieList, Movie
from api.genres import GenreList, Genre
from api.directors import DirectorList, Director
from api.actors import ActorList, Actor
from uuid import uuid4

# API URL
API_VERSION = 1
API_BASE_URL = f"/api/v{API_VERSION}"

# Globals
app = Flask(__name__)
app.config['SECRET_KEY'] = uuid4()
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

# CORS
cors = CORS(app, resources={
            r"/api/*": {"origins": "*"}})


# Error Handler
@ app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# API Resources

# Actors
api.add_resource(ActorList, f"{API_BASE_URL}/actors")
api.add_resource(
    Actor, f"{API_BASE_URL}/actors/<string:actorID>")

# Directors
api.add_resource(DirectorList, f"{API_BASE_URL}/directors")
api.add_resource(
    Director, f"{API_BASE_URL}/directors/<string:directorID>")

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


# App Runner
if __name__ == '__main__':
    app.run(port=5000, debug=True)

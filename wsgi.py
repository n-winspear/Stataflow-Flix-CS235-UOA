#!flask/bin/python
from flask import Flask, jsonify, make_response, session
from flask_restful import Api
from flask_session import Session
from adapters.memoryrepository import MemoryRepository
from api_routes.reviews import ReviewList, Review
from api_routes.ratings import RatingList, Rating
from api_routes.movies import MovieList, Movie
from api_routes.genres import GenreList, Genre
from api_routes.directors import DirectorList, Director
from api_routes.actors import ActorList, Actor

# Globals
app = Flask(__name__)
api = Api(app)
Session(app)

# Configs
app.config['SESSION_TYPE'] = 'redis'
session['MEMORY_REPO'] = MemoryRepository()
session['API_VERSION'] = 1
session['API_BASE_URL'] = f"/api/v{session['API_VERISON']}"

# Error Handler


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# API Resources

# Actors
api.add_resource(ActorList, f"{session['API_BASE_URL']}/actors")
api.add_resource(
    Actor, f"{session['API_BASE_URL']}/actors/<string:actorID>")

# Directors
api.add_resource(DirectorList, f"{session['API_BASE_URL']}/directors")
api.add_resource(
    Director, f"{session['API_BASE_URL']}/directors/<string:directorID>")

# Genres
api.add_resource(GenreList, f"{session['API_BASE_URL']}/genres")
api.add_resource(
    Genre, f"{session['API_BASE_URL']}/genres/<string:genreID>")

# Movies
api.add_resource(MovieList, f"{session['API_BASE_URL']}/movies")
api.add_resource(
    Movie, f"{session['API_BASE_URL']}/movies/<string:movieID>")

# Ratings
api.add_resource(RatingList, f"{session['API_BASE_URL']}/ratings")
api.add_resource(
    Rating, f"{session['API_BASE_URL']}/ratings/<string:ratingID>")

# Reviews
api.add_resource(ReviewList, f"{session['API_BASE_URL']}/reviews")
api.add_resource(
    Review, f"{session['API_BASE_URL']}/reviews/<string:reviewID>")


# App Runner
if __name__ == '__main__':
    app.run(port=5000, debug=True)

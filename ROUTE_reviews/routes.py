from flask import Blueprint, make_response, jsonify, request
from flask_cors import cross_origin
from adapters.memoryrepository import MemoryRepository
from domain_models.review import Review
from domain_models.movie import Movie

bp = Blueprint('route_reviews', __name__)
repo = MemoryRepository()

api_version = 1
api_URL = f"/api/v{api_version}/reviews"


@bp.route(f'{api_URL}/all', methods=['GET'])
@cross_origin()
def get_all_reviews():
    response = {
        "reviews": repo.get_all_reviews(),
    }
    return make_response(jsonify(response)), 200


@bp.route(f'{api_URL}', methods=['POST'])
@cross_origin()
def add_review():
    content = request.get_json()
    response = {
        "successful": False,
        "movie": content['movie'],
        "rating": content['rating'],
        "reviewText": content['reviewText']
    }
    response['successful'] = True if repo.add_review(
        Review(Movie(content['movie']), content['rating'], content['reviewText'])) else False,
    if response['successful']:
        return make_response(jsonify(response)), 201
    else:
        return make_response(jsonify(response)), 400

from flask import Blueprint, make_response, jsonify
from flask_cors import cross_origin
from adapters.memoryrepository import MemoryRepository

bp = Blueprint('route_movies', __name__)
repo = MemoryRepository()

api_version = 1
api_URL = f"/api/v{api_version}/movies"


@bp.route(f'{api_URL}/all', methods=['GET'])
@cross_origin()
def index():
    response = {
        "movies": repo.get_all_movies(),
    }
    return make_response(jsonify(response)), 200

from flask import Blueprint, make_response
from adapters.memoryrepository import MemoryRepository

bp = Blueprint('home_blueprint', __name__)

repo = MemoryRepository()


@bp.route('/', methods=['GET'])
def index():
    movies = repo.get_all_movies()
    reviews = repo.get_all_reviews()

    return make_response()

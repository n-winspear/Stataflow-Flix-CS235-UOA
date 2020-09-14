from flask import Blueprint, make_response

bp = Blueprint('home_blueprint', __name__)


@bp.route('/', methods=['GET'])
def index():
    return None

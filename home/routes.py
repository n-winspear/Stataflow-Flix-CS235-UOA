from flask import Blueprint, make_response
import home.services as s
from flask import jsonify

bp = Blueprint('home_blueprint', __name__)


@bp.route('/', methods=['GET'])
def index():
    response = s.get_home_data()
    return make_response(jsonify(response)), 200

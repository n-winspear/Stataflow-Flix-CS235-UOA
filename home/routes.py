from flask import Blueprint, make_response
import home.services as s
from flask import jsonify
from flask_cors import cross_origin

bp = Blueprint('home_blueprint', __name__)

api_version = 1
api_URL = f"/api/v{api_version}/"


@bp.route(f'{api_URL}/home', methods=['GET'])
@cross_origin()
def index():
    response = s.get_home_data()
    return make_response(jsonify(response)), 200

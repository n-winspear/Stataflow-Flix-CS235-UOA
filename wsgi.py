#!flask/bin/python
from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from data_processors.moviecsvparser import MovieCSVParser
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


with app.app_context():
    from ROUTE_movies import routes
    app.register_blueprint(routes.bp)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

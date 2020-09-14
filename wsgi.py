from flask import Flask
from data_processors.moviecsvparser import MovieCSVParser

file_path = 'data_processors/Data1000Movies.csv'

fp = MovieCSVParser(file_name=file_path)
fp.read_csv_file()

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World</h1>"


app.run(port=5000, debug=True)

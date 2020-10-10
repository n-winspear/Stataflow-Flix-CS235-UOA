from adapters.abstractrepository import AbstractRepository
from data_processors.moviecsvparser import MovieCSVParser
from domain_models.actor import Actor
from domain_models.director import Director
from domain_models.genre import Genre
from domain_models.movie import Movie
from domain_models.review import Review
from domain_models.rating import Rating
import os
import json


class MemoryRepository(AbstractRepository):

    def __init__(self):

        # JSON DB Path
        self.__json_db_file_path = './StataflowFlixDB.json'

        # Initialising
        if not os.path.exists(self.__json_db_file_path):
            CSV_FILE_PATH = 'data_processors/Data1000Movies.csv'
            fp = MovieCSVParser(CSV_FILE_PATH)
            fp.read_csv_file()
            self._dataset_of_actors = fp.dataset_of_actors
            self._dataset_of_movies = fp.dataset_of_movies
            self._dataset_of_directors = fp.dataset_of_directors
            self._dataset_of_genres = fp.dataset_of_genres
            self._dataset_of_reviews = fp.dataset_of_reviews
            self._dataset_of_ratings = fp.dataset_of_ratings
            self.__write_json_db
        else:
            self.__read_json_db

    # Writing JSON DB
    def __write_json_db(self):
        with open(self.__json_db_file_path, "w") as db_json:
            db_struct = {
                "actors": self._dataset_of_directors,
                "movies": self._dataset_of_movies,
                "directors": self._dataset_of_directors,
                "genres": self._dataset_of_genres,
                "reviews": self._dataset_of_reviews,
                "ratings": self._dataset_of_ratings
            }
            json.dumps(db_struct, db_json)

    # Reading JSON DB
    def __read_json_db(self):
        with open(self.__json_db_file_path, "r") as db_json:
            db = json.loads(db_json)
            self._dataset_of_actors = db['actors']
            self._dataset_of_movies = db['movies']
            self._dataset_of_directors = db['directors']
            self._dataset_of_genres = db['genres']
            self._dataset_of_reviews = db['reviews']
            self._dataset_of_ratings = db['ratings']

    ###############################################
    # Actor Methods
    ###############################################

    # GET

    def get_actor(self, personID: str):
        for stored_actor in self._dataset_of_actors:
            if stored_actor.personID == personID:
                return stored_actor.toJSON()

    # INSERT
    def add_actor(self, actor: Actor):
        if isinstance(actor, Actor):
            self._dataset_of_actors.append(actor)
            self.__write_json_db()
            return True
        return False

    # UPDATE
    def update_actor(self, updated_actor: Actor):
        if isinstance(updated_actor, Actor):
            [updated_actor if actor.personID ==
                updated_actor.personID else actor for actor in self._dataset_of_actors]
            self.__write_json_db()

    # DELETE
    def delete_actor(self, personID: str):
        for actor in self._dataset_of_actors:
            if actor.personID == personID:
                self._dataset_of_actors.remove(actor)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_actors(self):
        json_actors = []
        for actor in self._dataset_of_actors:
            json_actors.append(actor.toJSON())
        return json_actors

    # INSERT MULTIPLE
    def insert_multiple_actors(self, actors: list):
        for actor in actors:
            if isinstance(actor, Actor) and actor not in self._dataset_of_actors:
                self._dataset_of_actors.append(actor)
        self.__write_json_db()

    ###############################################
    # Director Methods
    ###############################################

    # GET
    def get_director(self, personID: str):
        for stored_director in self._dataset_of_directors:
            if stored_director.personID == personID:
                return stored_director.toJSON()

    # INSERT
    def add_director(self, director: Director):
        if isinstance(director, Director):
            self._dataset_of_directors.append(director)
            self.__write_json_db()
            return True
        return False

    # UPDATE
    def update_director(self, updated_director: Director):
        if isinstance(updated_director, Director):
            [updated_director if director.personID ==
                updated_director.personID else director for director in self._dataset_of_directors]
            self.__write_json_db()

    # DELETE
    def delete_director(self, personID: str):
        for director in self._dataset_of_directors:
            if director.personID == personID:
                self._dataset_of_directors.remove(director)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_directors(self):
        json_directors = []
        for director in self._dataset_of_directors:
            json_directors.append(director.toJSON())
        return json_directors

    # INSERT MULTIPLE
    def insert_multiple_directors(self, directors: list):
        for director in directors:
            if isinstance(director, Director) and director not in self._dataset_of_directors:
                self._dataset_of_directors.append(director)
        self.__write_json_db()

    ###############################################
    # Genre Methods
    ###############################################

    # GET
    def get_genre(self, genreID: str):
        for stored_genre in self._dataset_of_genres:
            if stored_genre.genreID == genreID:
                return stored_genre.toJSON()

    # INSERT
    def add_genre(self, genre: Genre):
        if isinstance(genre, Genre):
            self._dataset_of_genres.append(genre)
            self.__write_json_db()
            return True
        return False

    # UPDATE
    def update_genre(self, updated_genre: Genre):
        if isinstance(updated_genre, Genre):
            [updated_genre if genre.movieID ==
                updated_genre.genreID else genre for genre in self._dataset_of_genres]
            self.__write_json_db()

    # DELETE
    def delete_genre(self, genreID: str):
        for genre in self._dataset_of_genres:
            if genre.genreID == genreID:
                self._dataset_of_genres.remove(genre)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_genres(self):
        json_genres = []
        for genre in self._dataset_of_genres:
            json_genres.append(genre.toJSON())
        return self._dataset_of_genres

    # INSERT MULTIPLE
    def insert_multiple_genres(self, genres: list):
        for genre in genres:
            if isinstance(genre, Genre) and genre not in self._dataset_of_genres:
                self._dataset_of_genres.append(genre)
        self.__write_json_db()

    ###############################################
    # Movie Methods
    ###############################################

    # GET
    def get_movie(self, movieID: str):
        for stored_movie in self._dataset_of_movies:
            if stored_movie.movieID == movieID:
                return stored_movie.toJSON()

    # INSERT
    def add_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            self._dataset_of_movies.append(movie)
            self.__write_json_db()
            return True
        return False

    # UPDATE
    def update_movie(self, updated_movie: Movie):
        if isinstance(updated_movie, Movie):
            [updated_movie if movie.movieID ==
                updated_movie.movieID else movie for movie in self._dataset_of_movies]
            self.__write_json_db()

    # DELETE
    def delete_movie(self, movieID: str):
        for movie in self._dataset_of_movies:
            if movie.movieID == movieID:
                self._dataset_of_movies.remove(movie)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_movies(self):
        json_movies = []
        for movie in self._dataset_of_movies:
            json_movies.append(movie.toJSON())
        return json_movies

    # INSERT MULTIPLE
    def insert_multiple_movies(self, movies: list):
        for movie in movies:
            if isinstance(movie, Movie) and movie not in self._dataset_of_movies:
                self._dataset_of_movies.append(movie)
        self.__write_json_db()

    ###############################################
    # Review Methods
    ###############################################

    # GET
    def get_review(self, reviewID: str):
        for stored_review in self._dataset_of_reviews:
            if stored_review.reviewID == reviewID:
                return stored_review.toJSON()

    # INSERT
    def add_review(self, review: Review):
        if isinstance(review, Review):
            self._dataset_of_reviews.append(review)
            self.__write_json_db()
            return True
        return False

    # UPDATE
    def update_review(self, updated_review: Review):
        if isinstance(updated_review, Review):
            [updated_review if updated_review.reviewID ==
                review.reviewID else review for review in self._dataset_of_review]
            self.__write_json_db()

    # DELETE
    def delete_review(self, reviewID: str):
        for review in self._dataset_of_reviews:
            if review.reviewID == reviewID:
                self._dataset_of_reviews.remove(review)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_reviews(self):
        json_reviews = []
        for review in self._dataset_of_reviews:
            json_reviews.append(review.toJSON())
        return json_reviews

    # INSERT MULTIPLE
    def insert_multiple_reviews(self, reviews: list):
        for review in reviews:
            if isinstance(review, Review) and review not in self._dataset_of_reviews:
                self._dataset_of_reviews.append(review)
        self.__write_json_db()

    ###############################################
    # Rating Methods
    ###############################################

    # GET
    def get_rating(self, ratingID: str):
        for stored_rating in self._dataset_of_ratings:
            if stored_rating.ratingID == ratingID:
                return stored_rating.toJSON()

    # INSERT
    def add_rating(self, rating: Rating):
        if isinstance(rating, Rating):
            self._dataset_of_ratings.append(rating)
            self.__write_json_db()
            return True
        return False

    # UPDATE
    def update_rating(self, updated_rating: Rating):
        if isinstance(updated_rating, Rating):
            [updated_rating if updated_rating.ratingID ==
                rating.ratingID else rating for rating in self._dataset_of_rating]
            self.__write_json_db()

    # DELETE
    def delete_rating(self, ratingID: str):
        for rating in self._dataset_of_ratings:
            if rating.ratingID == ratingID:
                self._dataset_of_ratings.remove(rating)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_ratings(self):
        json_ratings = []
        for rating in self._dataset_of_ratings:
            json_ratings.append(rating.toJSON())
        return json_ratings

    # INSERT MULTIPLE
    def insert_multiple_ratings(self, ratings: list):
        for rating in ratings:
            if isinstance(rating, Rating) and rating not in self._dataset_of_ratings:
                self._dataset_of_ratings.append(rating)
            self.__write_json_db()

    ###############################################
    # User Methods
    ###############################################

    # IMPLEMENT THESE

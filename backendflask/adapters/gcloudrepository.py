from backendflask.adapters.abstractrepository import AbstractRepository
from backendflask.data_processors.moviecsvparser import MovieCSVParser
from backendflask.domain_models.actor import Actor
from backendflask.domain_models.director import Director
from backendflask.domain_models.genre import Genre
from backendflask.domain_models.movie import Movie
from backendflask.domain_models.review import Review
from backendflask.domain_models.rating import Rating
from backendflask.domain_models.user import User
from mysql.connector.constants import ClientFlag
import mysql.connector
import os
import json


class GCloudRepository(AbstractRepository):

    def __init__(self):

        self.__db_config = {
            'user': 'root',
            'password': 'F6b#CkG5pybYKBaIf1Ua',  # Move this to env when db working
            'host': '35.197.160.250',
            'client_flags': [ClientFlag.SSL],
            'database': 'SFX_DB',
            'ssl_ca': 'gcloud-config-files/server-ca.pem',
            'ssl_cert': 'gcloud-config-files/client-cert.pem',
            'ssl_key': 'gcloud-config-files/client-key.pem'
        }

        self.__cnxn = mysql.connector.connect(**self.__db_config)
        self.__crsr = self.__cnxn.cursor()

        self.__initial_db = True

        if self.__initial_db == True:
            self.__fresh_db()

    def __fresh_db(self):
        self.__crsr.execute("""CREATE_TABLE Actors (
            personID VARCHAR(255) PRIMARY KEY,
            fullName VARCHAR(255),
            gender INTEGER,
            dateOfBirth VARCHAR(255),
            imdbPage VARCHAR(255)
        )""")

        self.__crsr.execute("""CREATE_TABLE Directors (
            personID VARCHAR(255) PRIMARY KEY,
            fullName VARCHAR(255),
            gender INTEGER,
            dateOfBirth VARCHAR(255),
            imdbPage VARCHAR(255)
        )""")

        self.__crsr.execute("""CREATE_TABLE Genres (
            genreID VARCHAR(255) PRIMARY KEY,
            genreName VARCHAR(255),
        )""")

        self.__crsr.execute("""CREATE_TABLE Movie (
            movieID VARCHAR(255) PRIMARY KEY,
            movieTitle VARCHAR(255),
            releaseYear INTEGER,
            genres VARCHAR(255),
            description VARCHAR(510),
            directorID VARCHAR(255),
            actorID VARCHAR(255),
            runtimeMinutes INTEGER,
            averageRating FLOAT,
            voteCount INTEGER,
            revenue INTEGER,
            metascore FLOAT,
        )""")

        self.__crsr.execute("""CREATE_TABLE Rating (
            ratingID VARCHAR(255) PRIMARY KEY,
            personID VARCHAR(255),
            movieTitle VARCHAR(255),
            rating FLOAT
        )""")

        self.__crsr.execute("""CREATE_TABLE Review (
            reviewID VARCHAR(255) PRIMARY KEY,
            personID VARCHAR(255),
            movieTitle VARCHAR(255),
            reviewText VARCHAR(1020)
        )""")

        self.__crsr.execute("""CREATE_TABLE User (
            personID VARCHAR(255) PRIMARY KEY,
            firstName VARCHAR(255),
            lastName VARCHAR(255),
            gender INTEGER,
            emailAddress VARCHAR(510),
            password VARCHAR(255),
            phoneNumber VARCHAR(255),
            watchlist VARCHAR(255),
            watchedMovies VARCHAR(255),
            reviews VARCHAR(255),
        )""")

        ###############################################
        # PROPERTIES
        ###############################################

    @ property
    def dataset_of_actors(self):
        return self._dataset_of_actors

    @ property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @ property
    def dataset_of_directors(self):
        return self._dataset_of_directors

    @ property
    def dataset_of_genres(self):
        return self._dataset_of_genres

    @ property
    def dataset_of_reviews(self):
        return self._dataset_of_reviews

    @ property
    def dataset_of_ratings(self):
        return self._dataset_of_ratings

    @ property
    def dataset_of_users(self):
        return self._dataset_of_users

    ###############################################
    # Actor Methods
    ###############################################

    # GET

    def get_actor(self, personID: str):
        for stored_actor in self._dataset_of_actors:
            if stored_actor.personID == personID:
                return stored_actor

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
        return self._dataset_of_actors

    ###############################################
    # Director Methods
    ###############################################

    # GET

    def get_director(self, personID: str):
        for stored_director in self._dataset_of_directors:
            if stored_director.personID == personID:
                return stored_director

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
        return self._dataset_of_directors

    ###############################################
    # Genre Methods
    ###############################################

    # GET
    def get_genre(self, genreID: str):
        for stored_genre in self._dataset_of_genres:
            if stored_genre.genreID == genreID:
                return stored_genre

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
            [updated_genre if genre.genreID ==
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
        return self._dataset_of_genres

    ###############################################
    # Movie Methods
    ###############################################

    # GET

    def get_movie(self, movieID: str):
        for stored_movie in self._dataset_of_movies:
            if stored_movie.movieID == movieID:
                return stored_movie

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
        return self._dataset_of_movies

    ###############################################
    # Review Methods
    ###############################################

    # GET

    def get_review(self, reviewID: str):
        for stored_review in self._dataset_of_reviews:
            if stored_review.reviewID == reviewID:
                return stored_review

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
                review.reviewID else review for review in self._dataset_of_reviews]
            self.__write_json_db()

    # DELETE
    def delete_review(self, reviewID: str):
        for review in self._dataset_of_reviews:
            print(review, review.reviewID)
            if review.reviewID == reviewID:
                self._dataset_of_reviews.remove(review)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_reviews(self):
        return self._dataset_of_reviews

    ###############################################
    # Rating Methods
    ###############################################

    # GET

    def get_rating(self, ratingID: str):
        for stored_rating in self._dataset_of_ratings:
            if stored_rating.ratingID == ratingID:
                return stored_rating

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
                rating.ratingID else rating for rating in self._dataset_of_ratings]
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
        return self._dataset_of_ratings

    ###############################################
    # User Methods
    ###############################################

    # GET

    def get_user(self, personID: str):
        for stored_user in self._dataset_of_users:
            if stored_user.personID == personID:
                return stored_user

    # INSERT
    def add_user(self, user: User):
        if isinstance(user, User):
            self._dataset_of_users.append(user)
            self.__write_json_db()
            return True
        return False

    # UPDATE
    def update_user(self, updated_user: User):
        if isinstance(updated_user, User):
            [updated_user if updated_user.personID ==
                user.personID else user for user in self._dataset_of_users]
            self.__write_json_db()

    # DELETE
    def delete_user(self, personID: str):
        for user in self._dataset_of_users:
            if user.personID == personID:
                self._dataset_of_users.remove(user)
                self.__write_json_db()
                return True
        return False

    # GET ALL
    def get_all_users(self):
        return self._dataset_of_users

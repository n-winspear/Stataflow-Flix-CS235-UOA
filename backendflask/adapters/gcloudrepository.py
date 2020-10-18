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
            'user': 'sfx',
            # 'password': 'F6b#CkG5pybYKBaIf1Ua',  # Move this to env when db working
            'host': '35.197.160.250',
            'database': 'SFX_DB',
        }

        self.__cnxn = mysql.connector.connect(**self.__db_config)
        self.__crsr = self.__cnxn.cursor()

        #self.__initial_db = True

        # if self.__initial_db == True:
        #   self.__fresh_db()

    def __fresh_db(self):

        self.__crsr.execute("""DROP TABLE IF EXISTS Actor;""")
        self.__crsr.execute("""DROP TABLE IF EXISTS Director;""")
        self.__crsr.execute("""DROP TABLE IF EXISTS Genre;""")
        self.__crsr.execute("""DROP TABLE IF EXISTS Movie;""")
        self.__crsr.execute("""DROP TABLE IF EXISTS Rating;""")
        self.__crsr.execute("""DROP TABLE IF EXISTS Review;""")
        self.__crsr.execute("""DROP TABLE IF EXISTS User;""")

        self.__crsr.execute("""CREATE TABLE Actor(
            personID VARCHAR(255) PRIMARY KEY,
            fullName VARCHAR(255),
            gender INTEGER,
            dateOfBirth VARCHAR(255),
            imdbPage VARCHAR(255)
        );""")

        self.__crsr.execute("""CREATE TABLE Director(
            personID VARCHAR(255) PRIMARY KEY,
            fullName VARCHAR(255),
            gender INTEGER,
            dateOfBirth VARCHAR(255),
            imdbPage VARCHAR(255)
        );""")

        self.__crsr.execute("""CREATE TABLE Genre(
            genreID VARCHAR(255) PRIMARY KEY,
            genreName VARCHAR(255)
        );""")

        self.__crsr.execute("""CREATE TABLE Movie(
            movieID VARCHAR(255) PRIMARY KEY,
            movieTitle VARCHAR(255),
            releaseYear INTEGER,
            genres VARCHAR(255),
            description VARCHAR(510),
            directors VARCHAR(255),
            actors VARCHAR(255),
            runtimeMinutes INTEGER,
            averageRating FLOAT,
            voteCount INTEGER,
            revenue INTEGER,
            metascore FLOAT
        );""")

        self.__crsr.execute("""CREATE TABLE Rating(
            ratingID VARCHAR(255) PRIMARY KEY,
            personID VARCHAR(255),
            movieTitle VARCHAR(255),
            rating FLOAT
        );""")

        self.__crsr.execute("""CREATE TABLE Review(
            reviewID VARCHAR(255) PRIMARY KEY,
            personID VARCHAR(255),
            movieTitle VARCHAR(255),
            reviewText VARCHAR(1020)
        );""")

        self.__crsr.execute("""CREATE TABLE User(
            personID VARCHAR(255) PRIMARY KEY,
            firstName VARCHAR(255),
            lastName VARCHAR(255),
            gender INTEGER,
            emailAddress VARCHAR(510),
            password VARCHAR(255),
            phoneNumber VARCHAR(255),
            watchlist VARCHAR(255),
            watchedMovies VARCHAR(255),
            reviews VARCHAR(255)
        );""")

    ###############################################
    # Actor Methods
    ###############################################

    # GET

    def get_actor(self, personID: str):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Actor WHERE personID = '{personID}';""")
        print(dbRes)

    # INSERT
    def add_actor(self, actor: Actor):
        dbRes = self.__crsr.execute(
            f"""INSERT INTO Actor(
                personID,
                fullName,
                gender,
                dateOfBirth,
                imdbPage
            ) VALUES(
                '{actor.personID}',
                '{actor.full_name}',
                {actor.gender},
                '{actor.date_of_birth}',
                '{actor.imdb_page}'
            );""")
        print(dbRes)

    # UPDATE
    def update_actor(self, updated_actor: Actor):
        dbRes = self.__crsr.execute(
            f"""Update Actor SET(
                fullName='{updated_actor.full_name}',
                gender={updated_actor.gender},
                dateOfBirth='{updated_actor.date_of_birth}',
                imdbPage='{updated_actor.imdb_page}'
            ) WHERE personID = '{updated_actor.personID}';""")
        print(dbRes)

    # DELETEs
    def delete_actor(self, personID: str):
        dbRes = self.__crsr.execute(
            f"""DELETE FROM Actor WHERE personID = '{personID}';""")
        print(dbRes)

    # GET ALL
    def get_all_actors(self):
        return self._dataset_of_actors

    ###############################################
    # Director Methods
    ###############################################

    # GET

    def get_director(self, personID: str):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Director WHERE personID = '{personID}';""")
        print(dbRes)
    # INSERT

    def add_director(self, director: Director):
        dbRes = self.__crsr.execute(
            f"""INSERT INTO Director(
                personID,
                fullName,
                gender,
                dateOfBirth,
                imdbPage
            ) VALUES(
                '{director.personID}',
                '{director.full_name}',
                {director.gender},
                '{director.date_of_birth}',
                '{director.imdb_page}'
            );""")
        print(dbRes)

    # UPDATE
    def update_director(self, updated_director: Director):
        dbRes = self.__crsr.execute(
            f"""Update Director SET(
                fullName='{updated_director.full_name}',
                gender={updated_director.gender},
                dateOfBirth='{updated_director.date_of_birth}',
                imdbPage='{updated_director.imdb_page}'
            ) WHERE personID = '{updated_director.personID}';""")
        print(dbRes)

    # DELETE
    def delete_director(self, personID: str):
        dbRes = self.__crsr.execute(
            f"""DELETE FROM Director WHERE personID = '{personID}';""")
        print(dbRes)

    # GET ALL
    def get_all_directors(self):
        return self._dataset_of_directors

    ###############################################
    # Genre Methods
    ###############################################

    # GET
    def get_genre(self, genreID: str):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Genre WHERE genreID = '{genreID}';""")
        print(dbRes)

    # INSERT
    def add_genre(self, genre: Genre):
        dbRes = self.__crsr.execute(
            f"""INSERT INTO Genre(
                genreID,
                genreName
            ) VALUES(
                '{genre.genreID}',
                '{genre.genre_name}'
            );""")
        print(dbRes)

    # UPDATE
    def update_genre(self, updated_genre: Genre):
        dbRes = self.__crsr.execute(
            f"""UPDATE Genre SET (
                genreID = '{updated_genre.genreID}',
                genreName = '{updated_genre.genre_name}'
            );""")
        print(dbRes)

    # DELETE
    def delete_genre(self, genreID: str):
        dbRes = self.__crsr.execute(
            f"""DELETE FROM Genre WHERE genreID = '{genreID}';""")
        print(dbRes)

    # GET ALL
    def get_all_genres(self):
        return self._dataset_of_genres

    ###############################################
    # Movie Methods
    ###############################################

    # GET

    def get_movie(self, movieID: str):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Movie WHERE movieID = '{movieID}';""")
        print(dbRes)

    # INSERT
    def add_movie(self, movie: Movie):
        dbRes = self.__crsr.execute(
            f"""INSERT INTO Movie(
                movieID PRIMARY KEY,
                movieTitle,
                releaseYear,
                genres,
                description,
                directors,
                actors,
                runtimeMinutes,
                averageRating,
                voteCount,
                revenue,
                metascore
            ) VALUES(
                '{movie.movieID}',
                '{movie.title}',
                {movie.release_year},
                '{movie.genres}',
                '{movie.description}',
                '{movie.directors}',
                '{movie.actors}',
                {movie.runtime_minutes},
                {movie.average_rating},
                {movie.vote_count},
                {movie.revenue},
                {movie.meat}
            );""")
        print(dbRes)

    # UPDATE
    def update_movie(self, updated_movie: Movie):
        dbRes = self.__crsr.execute(
            f"""UPDATE Movie SET(
                movieTitle='{updated_movie.title}',
                releaseYear={updated_movie.release_year},
                genres='{updated_movie.genres}',
                description='{updated_movie.description}',
                directors='{updated_movie.directors}',
                actors='{updated_movie.actors}',
                runtimeMinutes={updated_movie.runtime_minutes},
                averageRating={updated_movie.average_rating},
                voteCount={updated_movie.vote_count},
                revenue={updated_movie.revenue},
                metascore={updated_movie.meat}
            );""")
        print(dbRes)

    # DELETE
    def delete_movie(self, movieID: str):
        dbRes = self.__crsr.execute(
            f"""DELETE FROM Movie WHERE movieID = '{movieID}';""")
        print(dbRes)

    # GET ALL
    def get_all_movies(self):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Movie;""")
        print(dbRes)

    ###############################################
    # Review Methods
    ###############################################

    # GET

    def get_review(self, reviewID: str):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM review WHERE reviewID = '{reviewID}';""")
        print(dbRes)

    # INSERT
    def add_review(self, review: Review):
        dbRes = self.__crsr.execute(
            f"""INSERT INTO Review (
                reviewID,
                personID,
                movieTitle,
                reviewText
            ) VALUES (
                '{review.reviewID}',
                '{review.personID}',
                '{review.movie.title}',
                '{review.review_text}'
            );""")
        print(dbRes)

    # UPDATE
    def update_review(self, updated_review: Review):
        dbRes = self.__crsr.execute(
            f"""UPDATE Review SET(
                personID='{updated_review.personID}',
                movieTitle='{updated_review.movie.title}',
                reviewText='{updated_review.review_text}',
            );""")
        print(dbRes)

    # DELETE
    def delete_review(self, reviewID: str):
        dbRes = self.__crsr.execute(
            f"""DELETE FROM Review WHERE reviewID = '{reviewID}';""")
        print(dbRes)

    # GET ALL
    def get_all_reviews(self):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Movie;""")
        print(dbRes)
    ###############################################
    # Rating Methods
    ###############################################

    # GET

    def get_rating(self, ratingID: str):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Rating WHERE ratingID = '{ratingID}';""")
        print(dbRes)

    # INSERT
    def add_rating(self, rating: Rating):
        dbRes = self.__crsr.execute(
            f"""INSERT INTO Rating(
                ratingID,
                personID,
                movieTitle,
                rating
            ) VALUES(
                '{rating.ratingID}',
                '{rating.personID}',
                '{rating.movie.title}',
                {rating.rating}
            );""")
        print(dbRes)

    # UPDATE
    def update_rating(self, updated_rating: Rating):
        dbRes = self.__crsr.execute(
            f"""UPDATE Rating SET(
                personID='{updated_rating.personID}',
                movieTitle='{updated_rating.movie.title}',
                rating={updated_rating.review_text}
            );""")
        print(dbRes)

    # DELETE
    def delete_rating(self, ratingID: str):
        dbRes = self.__crsr.execute(
            f"""DELETE FROM Rating WHERE ratingID = '{ratingID}';""")
        print(dbRes)

    # GET ALL
    def get_all_ratings(self):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM Movie;""")
        print(dbRes)

    ###############################################
    # User Methods
    ###############################################

    # GET

    def get_user(self, personID: str):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM User WHERE personID = '{personID}';""")
        print(dbRes)

    # INSERT
    def add_user(self, user: User):
        dbRes = self.__crsr.execute(
            f"""INSERT INTO User(
                personID,
                firstName,
                lastName,
                gender,
                emailAddress,
                password,
                phoneNumber,
                watchlist,
                watchedMovies,
                reviews
            ) VALUES(
                '{user.personID}',
                '{user.first_name}',
                '{user.last_name}',
                {user.gender},
                '{user.email_address}',
                '{user.password}',
                '{user.phone_number}',
                '{user.watchlist}',
                '{user.watched_movies}',
                '{user.reviews}'
            );""")
        print(dbRes)

    # UPDATE
    def update_user(self, updated_user: User):
        dbRes = self.__crsr.execute(
            f"""UPDATE User SET(
                firstName='{updated_user.first_name}',
                lastName='{updated_user.last_name}',
                gender={updated_user.gender},
                emailAddress='{updated_user.email_address}',
                password='{updated_user.password}',
                phoneNumber='{updated_user.phone_number}',
                watchlist='{updated_user.watchlist}',
                watchedMovies='{updated_user.watched_movies}',
                reviews='{updated_user.reviews}'
            ) WHERE personID = '{updated_user.personID}';""")

    # DELETE
    def delete_user(self, personID: str):
        dbRes = self.__crsr.execute(
            f"""DELETE FROM User WHERE personID = '{personID}';""")
        print(dbRes)

    # GET ALL
    def get_all_users(self):
        dbRes = self.__crsr.execute(
            f"""SELECT * FROM User;""")
        print(dbRes)

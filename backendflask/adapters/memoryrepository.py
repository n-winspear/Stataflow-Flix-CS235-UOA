from adapters.abstractrepository import AbstractRepository
from data_processors.moviecsvparser import MovieCSVParser
from domain_models.actor import Actor
from domain_models.director import Director
from domain_models.genre import Genre
from domain_models.movie import Movie
from domain_models.review import Review
from domain_models.rating import Rating
from domain_models.user import User
import os
import json


class MemoryRepository(AbstractRepository):

    def __init__(self):

        # JSON DB Path
        self.__json_db_file_path = './StataflowFlixDB.json'

        self._dataset_of_actors = []
        self._dataset_of_movies = []
        self._dataset_of_directors = []
        self._dataset_of_genres = []
        self._dataset_of_reviews = []
        self._dataset_of_ratings = []
        self._dataset_of_users = []

        self.__initalise_db()

    # Initialising
    def __initalise_db(self):
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

            self.__write_json_db()
        else:
            self.__read_json_db()

    # Writing JSON DB
    def __write_json_db(self):
        with open(self.__json_db_file_path, "w") as db_json:
            db_struct = {
                "actors": [actor.toJSON() for actor in self._dataset_of_actors],
                "movies": [movie.toJSON() for movie in self._dataset_of_movies],
                "directors": [director.toJSON() for director in self._dataset_of_directors],
                "genres": [genres.toJSON() for genres in self._dataset_of_genres],
                "reviews": [review.toJSON() for review in self._dataset_of_reviews],
                "ratings": [rating.toJSON() for rating in self._dataset_of_ratings],
                "users": [user.toJSON() for user in self._dataset_of_users]
            }
            json.dump(db_struct, db_json, indent=4)

    # Reading JSON DB
    def __read_json_db(self):
        with open(self.__json_db_file_path, "r") as db_json:
            db = json.load(db_json)
            self._dataset_of_actors = [Actor(personID=actor['personID'], full_name=actor['fullName'], gender=actor['gender'],
                                             date_of_birth=actor['dateOfBirth'], imdb_page=actor['imdbPage']) for actor in db['actors']]
            self._dataset_of_movies = [
                Movie(
                    movieID=movie['movieID'],
                    title=movie['movieTitle'],
                    release_year=movie['releaseYear'],
                    genres=[Genre(
                        genreID=genre['genreID'],
                        genre_name=genre['genreName']
                    ) for genre in movie['genres']],
                    description=movie['description'],
                    directors=[Director(
                        personID=director['personID'],
                        full_name=director['fullName'],
                        gender=director['gender'],
                        date_of_birth=director['dateOfBirth'],
                        imdb_page=director['imdbPage'],
                    ) for director in movie['directors']],
                    actors=[Actor(
                        personID=actor['personID'],
                        full_name=actor['fullName'],
                        gender=actor['gender'],
                        date_of_birth=actor['dateOfBirth'],
                        imdb_page=actor['imdbPage'],
                    ) for actor in movie['actors']],
                    runtime_minutes=movie['runtimeMinutes'],
                    average_rating=movie['averageRating'],
                    vote_count=movie['voteCount'],
                    revenue=movie['revenue'],
                    metascore=movie['metascore'],
                ) for movie in db['movies']]
            self._dataset_of_directors = [Director(
                personID=director['personID'],
                full_name=director['fullName'],
                gender=director['gender'],
                date_of_birth=director['dateOfBirth'],
                imdb_page=director['imdbPage'],
            ) for director in db['directors']]
            self._dataset_of_genres = [Genre(
                genreID=genre['genreID'],
                genre_name=genre['genreName'],
            ) for genre in db['genres']]
            self._dataset_of_reviews = [Review(
                reviewID=review['reviewID'],
                personID=review['personID'],
                movie=Movie(title=review['movieTitle']),
                review_text=review['reviewText'],
            ) for review in db['reviews']]
            self._dataset_of_ratings = [Rating(
                ratingID=rating['ratingID'],
                personID=rating['personID'],
                movie=Movie(title=rating['movieTitle']),
                rating=rating['rating'],
            ) for rating in db['ratings']]
            self._dataset_of_users = [User(
                first_name=user['firstName'],
                last_name=user['lastName'],
                personID=user['personID'],
                email_address=user['emailAddress'],
                password=user['password'],
                phone_number=user['phoneNumber'],
                gender=user['gender'],
                date_of_birth=user['dateOfBirth'],
                watchlist=[Movie(
                    movieID=movie['movieID'],
                    title=movie['movieTitle'],
                    release_year=movie['releaseYear'],
                    genres=[Genre(
                        genreID=genre['genreID'],
                        genre_name=genre['genreName']
                    ) for genre in movie['genres']],
                    description=movie['description'],
                    directors=[Director(
                        personID=director['personID'],
                        full_name=director['fullName'],
                        gender=director['gender'],
                        date_of_birth=director['dateOfBirth'],
                        imdb_page=director['imdbPage'],
                    ) for director in movie['directors']],
                    actors=[Actor(
                        personID=actor['personID'],
                        full_name=actor['fullName'],
                        gender=actor['gender'],
                        date_of_birth=actor['dateOfBirth'],
                        imdb_page=actor['imdbPage'],
                    ) for actor in movie['actors']],
                    runtime_minutes=movie['runtimeMinutes'],
                    average_rating=movie['averageRating'],
                    vote_count=movie['voteCount'],
                    revenue=movie['revenue'],
                    metascore=movie['metascore'],
                ) for movie in user['watchlist']],
                watched_movies=[Movie(
                    movieID=movie['movieID'],
                    title=movie['movieTitle'],
                    release_year=movie['releaseYear'],
                    genres=[Genre(
                        genreID=genre['genreID'],
                        genre_name=genre['genreName']
                    ) for genre in movie['genres']],
                    description=movie['description'],
                    directors=[Director(
                        personID=director['personID'],
                        full_name=director['fullName'],
                        gender=director['gender'],
                        date_of_birth=director['dateOfBirth'],
                        imdb_page=director['imdbPage'],
                    ) for director in movie['directors']],
                    actors=[Actor(
                        personID=actor['personID'],
                        full_name=actor['fullName'],
                        gender=actor['gender'],
                        date_of_birth=actor['dateOfBirth'],
                        imdb_page=actor['imdbPage'],
                    ) for actor in movie['actors']],
                    runtime_minutes=movie['runtimeMinutes'],
                    average_rating=movie['averageRating'],
                    vote_count=movie['voteCount'],
                    revenue=movie['revenue'],
                    metascore=movie['metascore'],
                ) for movie in user['watchedMovies']],
                reviews=[Review(
                    reviewID=review['reviewID'],
                    personID=review['personID'],
                    movie=Movie(title=review['movieTitle']),
                    review_text=review['reviewText'],
                ) for review in user['reviews']]
            ) for user in db['users']]

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
            print('made it here')
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

    def get_user(self, email_address: str):
        for stored_user in self._dataset_of_users:
            if stored_user.email_address == email_address:
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

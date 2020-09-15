import abc
from domain_models.actor import Actor
from domain_models.director import Director
from domain_models.genre import Genre
from domain_models.movie import Movie
from domain_models.review import Review


class AbstractRepository(abc.ABC):

    ###############################################
    # Actor Methods
    ###############################################

    # GET
    @abc.abstractmethod
    def get_actor(self, actor: Actor):
        raise NotImplementedError

    # INSERT
    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    # UPDATE
    @abc.abstractmethod
    def update_actor(self, actor: Actor):
        raise NotImplementedError

    # DELETE
    @abc.abstractmethod
    def delete_actor(self, actor: Actor):
        raise NotImplementedError

    # GET ALL
    @abc.abstractmethod
    def get_all_actors(self):
        raise NotImplementedError

    # INSERT MULTIPLE
    @abc.abstractmethod
    def insert_multiple_actors(self, actors: list):
        raise NotImplementedError

    ###############################################
    # Director Methods
    ###############################################

    # GET
    @abc.abstractmethod
    def get_director(self, director: Director):
        raise NotImplementedError

    # INSERT
    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError

    # UPDATE
    @abc.abstractmethod
    def update_director(self, director: Director):
        raise NotImplementedError

    # DELETE
    @abc.abstractmethod
    def delete_director(self, director: Director):
        raise NotImplementedError

    # GET ALL
    @abc.abstractmethod
    def get_all_directors(self):
        raise NotImplementedError

    # INSERT MULTIPLE
    @abc.abstractmethod
    def insert_multiple_directors(self, directors: list):
        raise NotImplementedError

    ###############################################
    # Genre Methods
    ###############################################

    # GET
    @abc.abstractmethod
    def get_genre(self, genre: Genre):
        raise NotImplementedError

    # INSERT
    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    # UPDATE
    @abc.abstractmethod
    def update_genre(self, genre: Genre):
        raise NotImplementedError

    # DELETE
    @abc.abstractmethod
    def delete_genre(self, genre: Genre):
        raise NotImplementedError

    # GET ALL
    @abc.abstractmethod
    def get_all_genres(self):
        raise NotImplementedError

    # INSERT MULTIPLE
    @abc.abstractmethod
    def insert_multiple_genres(self, genres: list):
        raise NotImplementedError

    ###############################################
    # Movie Methods
    ###############################################

    # GET
    @abc.abstractmethod
    def get_movie(self, movie: Movie):
        raise NotImplementedError

    # INSERT
    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    # UPDATE
    @abc.abstractmethod
    def update_movie(self, movie: Movie):
        raise NotImplementedError

    # DELETE
    @abc.abstractmethod
    def delete_movie(self, movie: Movie):
        raise NotImplementedError

    # GET ALL
    @abc.abstractmethod
    def get_all_movies(self):
        raise NotImplementedError

    # INSERT MULTIPLE
    @abc.abstractmethod
    def insert_multiple_movies(self, movies: list):
        raise NotImplementedError

    ###############################################
    # Review Methods
    ###############################################

    # GET
    @abc.abstractmethod
    def get_review(self, review: Review):
        raise NotImplementedError

    # INSERT
    @abc.abstractmethod
    def add_review(self, review: Review):
        raise NotImplementedError

    # UPDATE
    @abc.abstractmethod
    def update_review(self, review: Review):
        raise NotImplementedError

    # DELETE
    @abc.abstractmethod
    def delete_review(self, review: Review):
        raise NotImplementedError

    # GET ALL
    @abc.abstractmethod
    def get_all_reviews(self):
        raise NotImplementedError

    # INSERT MULTIPLE
    @abc.abstractmethod
    def insert_multiple_reviews(self, reviews: list):
        raise NotImplementedError

    ###############################################
    # User Methods
    ###############################################

    # IMPLEMENT THESE

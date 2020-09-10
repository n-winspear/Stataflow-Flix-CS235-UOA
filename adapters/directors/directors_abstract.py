from domain_models.director import Director
from domain_models.movie import Movie
import abc


class DirectorsAbstract(abc.ABC):

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

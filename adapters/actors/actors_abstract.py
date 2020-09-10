from domain_models.actor import Actor
from domain_models.movie import Movie
import abc


class ActorsAbstract(abc.ABC):

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

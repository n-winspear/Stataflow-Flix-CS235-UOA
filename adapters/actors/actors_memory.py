from domain_models.actor import Actor
from adapters.actors.actors_abstract import ActorsAbstract


class ActorsMemory(ActorsAbstract):

    def __init__(self):
        self.__actors = []

    # GET
    def get_actor(self, actor: Actor):
        matches = []

        for stored_actor in self.__actors:
            if actor == stored_actor:
                matches.append(stored_actor)
        return matches

    # INSERT
    def add_actor(self, actor: Actor):
        if isinstance(actor, Actor):
            self.__actors.append(actor)

    # UPDATE
    def update_actor(self, actor: Actor, new_actor_details: Actor):
        actor_details = self.get_actor(actor)

        # First Name Check
        if actor_details.first_name != new_actor_details.first_name:
            actor_details.first_name = new_actor_details.first_name

        # Last Name Check
        if actor_details.last_name != new_actor_details.last_name:
            actor_details.last_name = new_actor_details.last_name

        # Gender Check
        if actor_details.gender != new_actor_details.gender:
            actor_details.gender = new_actor_details.gender

        # Date Of Birth Check
        if actor_details.date_of_birth != new_actor_details.date_of_birth:
            actor_details.date_of_birth = new_actor_details.date_of_birth

        # Movies Acted In Check
        if actor_details.movies_acted_in != new_actor_details.movies_acted_in:
            actor_details.movies_acted_in = new_actor_details.movies_acted_in

        # IMDB Page Check
        if actor_details.imdb_page != new_actor_details.imdb_page:
            actor_details.imdb_page = new_actor_details.imdb_page

    # DELETE
    def delete_actor(self, actor: Actor):
        for stored_actor in self.__actors:
            if actor == stored_actor:
                self.__actors.remove(actor)

    # GET ALL
    def get_all_actors(self):
        return self.__actors

    # INSERT MULTIPLE
    def insert_multiple_actors(self, actors: list):
        for actor in actors:
            if isinstance(actor, Actor):
                self.__actors.append(actor)

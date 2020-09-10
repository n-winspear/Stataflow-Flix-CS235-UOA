from domain_models.director import Director
from domain_models.movie import Movie
from adapters.directors.directors_abstract import DirectorsAbstract


class DirectorsMemory(DirectorsAbstract):

    def __init__(self):
        self.__directors = []

    # GET
    def get_director(self, director: Director):
        matches = []

        for stored_director in self.__directors:
            if director == stored_director:
                matches.append(stored_director)
        return matches

    # INSERT
    def add_director(self, director: Director):
        if isinstance(director, Director):
            self.__directors.append(director)

    # UPDATE
    def update_director(self, director: Director, new_director_details: Director):
        director_details = self.get_director(director)

        # First Name Check
        if director_details.first_name != new_director_details.first_name:
            director_details.first_name = new_director_details.first_name

        # Last Name Check
        if director_details.last_name != new_director_details.last_name:
            director_details.last_name = new_director_details.last_name

        # Gender Check
        if director_details.gender != new_director_details.gender:
            director_details.gender = new_director_details.gender

        # Date Of Birth Check
        if director_details.date_of_birth != new_director_details.date_of_birth:
            director_details.date_of_birth = new_director_details.date_of_birth

        # Movies Acted In Check
        if director_details.movies_acted_in != new_director_details.directed_movies:
            director_details.movies_acted_in = new_director_details.directed_movies

        # IMDB Page Check
        if director_details.imdb_page != new_director_details.imdb_page:
            director_details.imdb_page = new_director_details.imdb_page

    # DELETE
    def delete_director(self, director: Director):
        for stored_director in self.__directors:
            if director == stored_director:
                self.__directors.remove(director)

    # GET ALL
    def get_all_directors(self):
        return self.__directors

    # INSERT MULTIPLE
    def insert_multiple_directors(self, directors: list):
        for director in directors:
            if isinstance(director, Director):
                self.__directors.append(director)

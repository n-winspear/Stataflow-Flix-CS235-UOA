from domain_models.person import Person
from domain_models.movie import Movie
import requests


class Actor(Person):
    def __init__(self, first_name: str = None, last_name: str = None, gender: int = None,  date_of_birth: datetime = None, IMDB_page: str = None, movies_acted_in: list = []):

        # Parent Class Call
        super(first_name, last_name, gender, date_of_birth)

        # IMDB Page
        self.__IMDB_page = IMDB_page.strip() if self.__valid_URL(IMDB_page) else None

        # Directed Movies
        self.__movies_acted_in = movies_acted_in if self.__valid_movies_acted_in(
            movies_acted_in) else self.__cleaned_movies_acted_in

    # Validators
    # Valid URL Check

    def __valid_URL(self, URL: str) -> str:
        try:
            response = requests.get(URL)
            return True

        except requests.ConnectionError as exception:
            return False

    # Movies Acted In Check
    def __valid_movies_acted_in(self, movies_acted_in: list) -> list:
        for movie in movies_acted_in:
            if isinstance(movie, Movie):
                return False
        return True

    # Movies Acted In Cleaner
    def __cleaned_movies_acted_in(self, movies_acted_in: list) -> list:

        cleaned_list = []

        for movie in movies_acted_in:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

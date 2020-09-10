from domain_models.person import Person
from domain_models.movie import Movie
import requests


class Director(Person):
    def __init__(self, first_name: str = None, last_name: str = None, gender: int = None,  date_of_birth: datetime = None, IMDB_page: str = None, directed_movies: list = []):

        # Parent Class Call
        super(first_name, last_name, gender, date_of_birth)

        # IMDB Page
        self.__IMDB_page = IMDB_page.strip() if self.__valid_URL(IMDB_page) else None

        # Directed Movies
        self.__directed_movies = directed_movies if self.__valid_directed_movies(
            directed_movies) else self.__cleaned_directed_movies

    # Validators
    # Valid URL Check

    def __valid_URL(self, URL: str) -> str:
        try:
            response = requests.get(URL)
            return True

        except requests.ConnectionError as exception:
            return False

    # Directed Movies Check
    def __valid_directed_movies(self, directed_movies: list) -> list:
        for movie in directed_movies:
            if isinstance(movie, Movie):
                return False
        return True

    # Directed Movies Cleaner
    def __cleaned_directed_movies(self, directed_movies: list) -> list:

        cleaned_list = []

        for movie in directed_movies:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

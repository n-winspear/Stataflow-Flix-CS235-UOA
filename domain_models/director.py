from domain_models.person import Person
import requests


class Director(Person):
    def __init__(self, first_name: str = None, last_name: str = None, gender: int = None,  date_of_birth: str = None, imdb_page: str = None, directed_movies: list = []):

        # Parent Class Call
        super().__init__(first_name, last_name, gender, date_of_birth)

        # IMDB Page
        self.__imdb_page = imdb_page.strip() if self.__valid_URL(imdb_page) else None

        # Directed Movies
        self.__directed_movies = directed_movies if self.__valid_directed_movies(
            directed_movies) else self.__cleaned_directed_movies

    def __str__(self):
        return f"First Name: {self.__first_name}\nLast Name: {self.__last_name}"

    def __repr__(self):
        return f"Director <{self.__last_name}, {self.__first_name}>"

    @property
    def imdb_page(self):
        return self.__imdb_page

    @imdb_page.setter
    def imdb_page(self, imdb_page: str) -> str:
        self.__imdb_page = imdb_page.strip() if self.__valid_URL(imdb_page) else None

    @property
    def directed_movies(self):
        return self.__directed_movies

    @directed_movies.setter
    def directed_movies(self, directed_movies: list) -> list:
        self.__directed_movies = directed_movies if self.__valid_directed_movies(
            directed_movies) else self.__cleaned_directed_movies

    # Validators
    # Valid URL Check
    def __valid_URL(self, URL: str) -> str:
        if not URL == None:
            try:
                response = requests.get(URL)
                return True

            except requests.ConnectionError as exception:
                return False

    # Directed Movies Check
    def __valid_directed_movies(self, directed_movies: list) -> list:
        from domain_models.movie import Movie

        for movie in directed_movies:
            if isinstance(movie, Movie):
                return False
        return True

    # Directed Movies Cleaner
    def __cleaned_directed_movies(self, directed_movies: list) -> list:
        from domain_models.movie import Movie

        cleaned_list = []

        for movie in directed_movies:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

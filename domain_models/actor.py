from domain_models.person import Person

import requests


class Actor(Person):
    def __init__(self, first_name: str = None, last_name: str = None, gender: int = None,  date_of_birth: str = None, imdb_page: str = None, movies_acted_in: list = []):

        # Parent Class Call
        super().__init__(first_name, last_name, gender, date_of_birth)

        # IMDB Page
        self.__imdb_page = imdb_page.strip() if self.__valid_URL(imdb_page) else None

        # Movies Acted In
        self.__movies_acted_in = movies_acted_in if self.__valid_movies_acted_in(
            movies_acted_in) else self.__cleaned_movies_acted_in

    def __str__(self):
        return f"First Name: {self.__first_name}\nLast Name: {self.__last_name}"

    def __repr__(self):
        return f"Actor <{self.__last_name}, {self.__first_name}>"

    @property
    def imdb_page(self):
        return self.__imdb_page

    @imdb_page.setter
    def imdb_page(self, imdb_page: str) -> str:
        self.__imdb_page = imdb_page.strip() if self.__valid_URL(imdb_page) else None

    @property
    def movies_acted_in(self):
        return self.__movies_acted_in

    @movies_acted_in.setter
    def movies_acted_in(self, movies_acted_in: list) -> list:
        self.__movies_acted_in = movies_acted_in if self.__valid_movies_acted_in(
            movies_acted_in) else self.__cleaned_movies_acted_in

    # Validators
    # Valid URL Check

    def __valid_URL(self, URL: str) -> str:
        if not URL == None:
            try:
                response = requests.get(URL)
                return True

            except requests.ConnectionError as exception:
                return False

    # Movies Acted In Check
    def __valid_movies_acted_in(self, movies_acted_in: list) -> list:
        from domain_models.movie import Movie
        for movie in movies_acted_in:
            if isinstance(movie, Movie):
                return False
        return True

    # Movies Acted In Cleaner
    def __cleaned_movies_acted_in(self, movies_acted_in: list) -> list:
        from domain_models.movie import Movie

        cleaned_list = []

        for movie in movies_acted_in:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

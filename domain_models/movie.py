from domain_models.actor import Actor
from domain_models.director import Director
from domain_models.genre import Genre
from datetime import datetime


class Movie:
    def __init__(self, title: str, release_year: int = None, genres: list = [], description: str = None, directors: list = [], actors: list = [], runtime_minutes: int = 0):

        # Title
        self.__title = title.strip() if type(title) == str else None

        # Release Year
        self.__release_year = release_year if self.__valid_release_year(
            release_year) else None

        # Genre
        self.__genre = genre if self.__valid_genres else self.__cleaned_genres

        # Description
        self.__description = description.strip() if type(description) == str else None

        # Directors
        self.__directors = directors if self.__valid_directors(
            directors) else self.__cleaned_directors(directors)

        # Actors
        self.__actors = actors if self.__valid_actors(
            actors) else self.__cleaned_actors(actors)

        # Runtime Minutes
        self.__runtime_minutes = runtime_minutes if (
            type(runtime_minutes) == int and runtime_minutes > 0) else 0

    def __str__(self):
        return f"Movie Title: {self.__title}\nRelease Year: {self.__release_year}\nRuntime: {self.__runtime_minutes} mins"

    def __repr__(self):
        return f"Movie <{self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return (self.__title == other.title) and (self.__directors == other.directors)

    def __hash__(self):
        return hash(f"{self.__titel}{self.__release_year}")

    # Properties
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str) -> str:
        self.__title = title.strip() if type(title) == str else None

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genres: list) -> list:
        self.__genre = genre if self.__valid_genres else self.__cleaned_genres

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str) -> str:
        self.__description = description.strip() if type(description) == str else None

    @property
    def directors(self):
        return self.__directors

    @directors.setter
    def directors(self, directors: list) -> list:
        self.__directors = directors if self.__valid_directors(
            directors) else self.__cleaned_directors(directors)

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actors: list) -> list:
        self.__actors = actors if self.__valid_actors(
            actors) else self.__cleaned_actors(directors)

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes: int) -> int:
        self.__runtime_minutes = runtime_minutes if (
            type(runtime_minutes) == int and runtime_minutes > 0) else 0

    # Validators
    # Actors Check
    def __valid_actors(self, actors: list) -> list:
        for actor in actors:
            if isinstance(actor, Actor):
                return False
        return True

    # Actors Cleaner
    def __cleaned_actors(self, actors: list) -> list:

        cleaned_list = []

        for actor in actors:
            if isinstance(actor, Actor):
                cleaned_list.append(actor)

        return cleaned_list

    # Directors Check
    def __valid_directors(self, directors: list) -> list:
        for director in directors:
            if isinstance(director, Director):
                return False
        return True

    # Directors Cleaner
    def __cleaned_directors(self, directors: list) -> list:

        cleaned_list = []

        for director in directors:
            if isinstance(director, Director):
                cleaned_list.append(director)

        return cleaned_list

    # Release Year Check
    def __valid_release_year(self, release_year: int) -> int:
        return release_year in range(1890, datetime.now().year)

    # Genres Check
    def __valid_genres(self, genres: list) -> list:
        for genre in genres:
            if isinstance(genre, Genre):
                return False
        return True

    # Genres Cleaner
    def __cleaned_genres(self, genres: list) -> list:

        cleaned_list = []

        for genre in genres:
            if isinstance(genre, Genre):
                cleaned_list.append(genre)

        return cleaned_list

    # Release Year Check
    def __valid_release_year(self, release_year: int) -> int:
        return release_year in range(1890, datetime.now().year)

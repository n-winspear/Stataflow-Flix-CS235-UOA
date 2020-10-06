from domain_models.actor import Actor
from domain_models.director import Director
from domain_models.genre import Genre
from datetime import datetime
from uuid import uuid4


class Movie:
    def __init__(self, title: str, movieID: str = uuid4(), release_year: int = None, genres: list = [], description: str = None, directors: list = [], actors: list = [], runtime_minutes: int = 0, average_rating: float = 0, vote_count: int = 0, revenue: float = 0.0, metascore: int = 0):

        # Unique ID
        self.__movieID = movieID

        # Title
        self.__title = title.strip() if type(title) == str else None

        # Release Year
        self.__release_year = release_year if self.__valid_release_year(
            release_year) else None

        # Genre
        self.__genres = genres if self.__valid_genres else self.__cleaned_genres

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

        # Average Rating
        self.__average_rating = average_rating if (
            type(average_rating) == float and average_rating in range(1, 11)) else 0

        # Vote Count
        self.__vote_count = vote_count if (
            type(vote_count) == int and vote_count > 0) else 0

        # Revenue
        self.__revenue = revenue if (
            type(revenue) == float and revenue > 0.0) else 0.0

        # Metascore
        self.__metascore = metascore if (
            type(metascore) == int and metascore in range(1, 101)) else 0

    def __str__(self):
        return f"Movie Title: {self.__title}\nRelease Year: {self.__release_year}\nRuntime: {self.__runtime_minutes} mins"

    def __repr__(self):
        return f"Movie <{self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return (self.__title == other.title) and (self.__directors == other.directors)

    def __hash__(self):
        return hash(f"{self.__title}{self.__release_year}")

    def toJSON(self):
        json_dump = {
            "movieID": self.__movieID,
            'movieTitle': self.__title,
            'releaseYear': self.__release_year,
            'genres': [genre.toJSON() for genre in self.__genres],
            'description': self.__description,
            'directors': [director.toJSON() for director in self.__directors],
            'actors': [actor.toJSON() for actor in self.__actors],
            'runtimeMinutes': self.__runtime_minutes,
            'averageRating': self.__average_rating,
            'voteCount': self.__vote_count,
            'revenue': self.__revenue,
            'metascore': self.__metascore
        }
        return json_dump

    # Properties
    @property
    def movieID(self):
        return self.__movieID

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str) -> str:
        self.__title = title.strip() if type(title) == str else None

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year: int) -> int:
        self.__release_year = release_year if self.__valid_release_year(
            release_year) else None

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres: list) -> list:
        self.__genres = genres if self.__valid_genres else self.__cleaned_genres

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

    @property
    def average_rating(self):
        return self.__average_rating

    @average_rating.setter
    def average_rating(self, average_rating: float) -> float:
        self.__average_rating = average_rating if (
            type(average_rating) == float and average_rating in range(1, 11)) else 0

    @property
    def vote_count(self):
        return self.__vote_count

    @vote_count.setter
    def vote_count(self, vote_count: int) -> int:
        self.__vote_count = vote_count if (
            type(vote_count) == int and vote_count > 0) else 0

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue: float) -> float:
        self.__revenue = revenue if (
            type(revenue) == float and revenue > 0.0) else 0.0

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, metascore: int) -> int:
        self.__metascore = metascore if (
            type(metascore) == int and metascore in range(1, 101)) else 0

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

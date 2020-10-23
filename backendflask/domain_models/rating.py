from backendflask.domain_models.movie import Movie
from uuid import uuid4


class Rating:

    def __init__(self, movie: Movie, ratingID: str = None, rating: float = None, personID: str = None):

        self.__ratingID = ratingID if ratingID else uuid4()

        self.__movie = movie if isinstance(movie, Movie) else None

        self.__rating = rating if (type(rating) == float and (
            rating > 0 and rating <= 10)) else None

        self.__personID = personID if personID else uuid4()

    def __str__(self):
        return f"Rating: {self.__rating}"

    def __repr__(self):
        return f"Rating <{self.__rating}>"

    def __eq__(self, other):
        return (self.__ratingID == other.ratingID)

    def __hash__(self):
        return hash(self.__ratingID)

    def toJSON(self):
        json_dump = {
            'ratingID': str(self.__ratingID),
            'personID': str(self.__personID),
            'movieTitle': self.__movie.title,
            'rating': self.__rating,
        }
        return json_dump

    # Properties

    @property
    def ratingID(self):
        return self.__ratingID

    @property
    def personID(self):
        return self.__personID

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating: str) -> str:
        self.__rating = rating if (
            type(rating) == float and (rating > 0 and rating <= 10)) else None

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie: Movie) -> Movie:
        self.__movie = movie if isinstance(movie, Movie) else None

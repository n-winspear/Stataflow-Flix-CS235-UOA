from backendflask.domain_models.movie import Movie
from uuid import uuid4


class Rating:
    def __init__(self, movie: Movie, ratingID: str = uuid4(),  rating: float = None, userID: str = uuid4()):

        # Rating ID
        self.__ratingID = ratingID if ratingID else uuid4()

        # Movie
        self.__movie = movie if isinstance(movie, Movie) else None

        # Rating
        self.__rating = rating if (
            type(rating) == float and (rating > 0 and rating <= 10)) else None

        # User ID
        self.__userID = userID if userID else uuid4()

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
            'ratingID': self.__ratingID,
            'userID': self.__userID,
            'movieTitle': self.__movie.title,
            'rating': self.__rating,
        }
        return json_dump

    # Properties

    @property
    def ratingID(self):
        return self.__ratingID

    @property
    def userID(self):
        return self.__userID

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

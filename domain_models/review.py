from domain_models.movie import Movie
from uuid import uuid4


class Review:
    def __init__(self, movie: Movie, reviewID: str = uuid4(), review_text: str = None, userID: str = None):

        # Review ID
        self.__reviewID = reviewID

        # User ID
        self.__userID = userID.strip() if type(userID) == str else None

        # Movie
        self.__movie = movie if isinstance(movie, Movie) else None

        # Review Text
        self.__review_text = review_text.strip() if type(review_text) == str else None

    def __str__(self):
        return f"Movie: {self.__movie}\n Text: {self.__review_text}"

    def __repr__(self):
        return f"Review <{self.__movie}, {self.__review_text}>"

    def __eq__(self, other):
        return (self.__reviewID == other.__reviewID)

    def __hash__(self):
        return hash(self.__reviewID)

    def toJSON(self):
        json_dump = {
            'userID': self.__userID,
            'reviewID': self.__reviewID,
            'movieTitle': self.__movie.title,
            'reviewText': self.__review_text,
        }
        return json_dump

    @property
    def reviewID(self):
        return self.__reviewID

    @property
    def userID(self):
        return self._userID

    @userID.setter
    def userID(self, userID):
        self._userID = userID.strip() if type(userID) == str else None

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie):
        self.self.__movie = movie if isinstance(movie, Movie) else None

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text):
        self.__review_text = review_text.strip() if type(review_text) == str else None

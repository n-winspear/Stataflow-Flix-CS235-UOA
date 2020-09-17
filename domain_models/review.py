from domain_models.movie import Movie


class Review:
    def __init__(self, movie: Movie, rating: float = None, review_text: str = None):

        # Movie
        self.__movie = movie if isinstance(movie, Movie) else None

        # Rating
        self.__rating = rating if 0 <= rating <= 10 else None

        # Review Text
        self.__review_text = review_text.strip() if type(review_text) == str else None

    def __str__(self):
        return f"Movie: {self.__movie}\nRating: {self.__rating}\n Text: {self.__review_text}"

    def __repr__(self):
        return f"Review <{self.__movie}, {self.__rating} | {self.__review_text}>"

    def __eq__(self, other):
        return (self.__movie == other.movie and self.__rating == other.rating and self.__review_text == other.review_text)

    def __hash__(self):
        return self.hash(f"{self.__movie}{self.__review_text}")

    def toJSON(self):
        json_dump = {
            'movieTitle': self.__movie.title,
            'rating': self.__rating,
            'reviewText': self.__review_text,
        }
        return json_dump

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie):
        self.self.__movie = movie if isinstance(movie, Movie) else None

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating if 0 <= rating <= 10 else None

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text):
        self.__review_text = review_text.strip() if type(review_text) == str else None

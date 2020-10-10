from uuid import uuid4


class Genre:
    def __init__(self, genre_name: str, genreID: str = None):

        # Genre ID
        self.__genreID = genreID if genreID else uuid4()

        # Genre Name
        self.__genre_name = genre_name.strip() if type(genre_name) == str else None

    def __str__(self):
        return f"Genre: {self.__genre_name}"

    def __repr__(self):
        return f"Genre <{self.__genre_name}>"

    def __eq__(self, other):
        return (self.__genre_name == other.genre_name)

    def __hash__(self):
        return hash(f"{self.__genreID}")

    def toJSON(self):
        json_dump = {
            'genreID': self.__genreID,
            'genreName': self.__genre_name,
        }
        return json_dump

    # Properties
    @property
    def genreID(self):
        return self.__genreID

    @property
    def genre_name(self):
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, genre_name: str) -> str:
        self.__genre_name = genre_name.strip() if type(genre_name) == str else None

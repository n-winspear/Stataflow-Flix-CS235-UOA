from backendflask.domain_models.person import Person
import requests


class Actor(Person):
    def __init__(self, full_name: str, personID: str = None, gender: int = None,  date_of_birth: str = None, imdb_page: str = None):

        # Parent Class Call
        super(Actor, self).__init__(
            full_name, personID, gender, date_of_birth)

        # IMDB Page
        self.__imdb_page = imdb_page.strip() if self.__valid_URL(imdb_page) else None

    def __str__(self):
        return f"Full Name: {self._full_name}"

    def __repr__(self):
        return f"Actor <{self._full_name}>"

    def __hash__(self):
        return hash(self._personID)

    def __eq__(self, other):
        return self._personID == other.personID

    def toJSON(self):
        json_dump = {
            'personID': str(self._personID),
            'fullName': self._full_name,
            'gender': self._gender,
            'dateOfBirth': self._date_of_birth,
            'imdbPage': self.__imdb_page,

        }
        return json_dump

    @property
    def imdb_page(self):
        return self.__imdb_page

    @imdb_page.setter
    def imdb_page(self, imdb_page: str) -> str:
        self.__imdb_page = imdb_page.strip() if self.__valid_URL(imdb_page) else None

    # Validators
    # Valid URL Check

    def __valid_URL(self, URL: str) -> str:
        if URL:
            try:
                response = requests.get(URL)
                return True

            except Exception as e:
                return False

from uuid import uuid4
from datetime import datetime


class Person(object):
    def __init__(self, full_name: str, personID: str = None, gender: int = 0,  date_of_birth: str = None):

        # Unique ID
        self._personID = personID if personID else uuid4()

        # Full Name
        self._full_name = full_name.strip() if type(full_name) == str else ""

        # Gender --> 1: Male, 2: Female, 3: Homosexual, 4: Bi-Sexual, 5: Other
        self._gender = gender if (isinstance(
            gender, int) and gender in (1, 2, 3, 4, 5)) else 1

        # Date of Birth
        try:
            self._date_of_birth = str(datetime.strptime(date_of_birth, '%d/%m/%Y').date()) if self.__valid_date_of_birth(
                datetime.strptime(date_of_birth, '%d/%m/%Y')) else None
        except Exception as e:
            print(e)
            self._date_of_birth = None

    def toJSON(self):
        json_dump = {
            'personID': f"{self._personID}",
            'fullName': self._full_name,
            'gender': self._gender,
            'dateOfBirth': self._date_of_birth,
        }
        return json_dump

    @property
    def personID(self):
        return self._personID

    @property
    def full_name(self):
        return f"{self._full_name}"

    @full_name.setter
    def full_name(self, full_name: str = "") -> str:
        self._full_name = full_name.strip() if type(full_name) == str else ""

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender: int = None) -> int:
        # Gender --> 1: Male, 2: Female, 3: Homosexual, 4: Bi-Sexual, 5: Other
        self._gender = gender if (isinstance(
            gender, int) and gender in (1, 2, 3, 4, 5)) else 1

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str = None) -> str:
        try:
            self._date_of_birth = str(datetime.strptime(date_of_birth, '%d/%m/%Y').date()) if self.__valid_date_of_birth(
                datetime.strptime(date_of_birth, '%d/%m/%Y')) else None
        except Exception as e:
            self._date_of_birth = None

    # Birthday Check
    def __valid_date_of_birth(self, date_of_birth):
        if (date_of_birth.year > 1900 and date_of_birth.year < datetime.now().year):
            return True

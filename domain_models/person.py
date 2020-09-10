from uuid import uuid4
from datetime import datetime


class Person:
    def __init__(self, first_name: str = None, last_name: str = None, gender: int = None,  date_of_birth: datetime = None):

        # Unique ID
        self.__unique_ID = uuid4()

        # First Name
        self.__first_name = first_name.strip().lower(
        ).capitalize() if type(first_name) == str else None

        # Last Name
        self.__last_name = last_name.strip().lower(
        ).capitalize() if type(last_name) == str else None

        # Gender --> 1: Male, 2: Female, 3: Homosexual, 4: Bi-Sexual, 5: Other
        self.__gender = gender if (isinstance(
            gender, int) and gender in (1, 2, 3, 4, 5)) else 1

        # Date of Birth
        try:
            self.__date_of_birth = datetime(date_of_birth) if self.__valid_date_of_birth(
                datetime(date_of_birth)) else None
        except Exception as e:
            print(f"Date of birth error: {e}")
            self.__date_of_birth = None

    def __str__(self):
        return f"First Name: {self.__first_name}\nLast Name: {self.__last_name}"

    def __repr__(self):
        return f"Person <{self.__last_name}, {self.__first_name}>"

    def __eq__(self, other):
        return self.__unique_ID == other.unique_ID

    def __hash__(self):
        return hash(self.__unique_ID)

    @property
    def unique_ID(self):
        return self.__unique_ID

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str = None) -> str:
        self.__first_name = first_name.strip().lower(
        ).capitalize() if type(first_name) == str else None

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str = None) -> str:
        self.__last_name = last_name.strip().lower(
        ).capitalize() if type(last_name) == str else None

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: int = None) -> int:
        # Gender --> 1: Male, 2: Female, 3: Homosexual, 4: Bi-Sexual, 5: Other
        self.__gender = gender if (isinstance(
            gender, int) and gender in (1, 2, 3, 4, 5)) else 1

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: datetime = None) -> datetime:
        try:
            self.__date_of_birth = datetime(date_of_birth) if self.__valid_date_of_birth(
                datetime(date_of_birth)) else None
        except Exception as e:
            print(f"Date of birth error: {e}")
            self.__date_of_birth = datetime(1970, 1, 1)

    # Birthday Check
    def __valid_date_of_birth(self, date_of_birth):
        if (date_of_birth.year > 1900 and date_of_birth < datetime.now().year):
            return True

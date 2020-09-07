from uuid import uuid4


class Person:
    def __init__(self, first_name: str = None, last_name: str = None):

        # Unique ID
        self.__unique_ID = uuid4()

        # First Name
        self.__first_name = first_name.strip().lower(
        ).capitalize() if type(first_name) == str else None

        # Last Name
        self.__last_name = last_name.strip().lower(
        ).capitalize() if type(last_name) == str else None

    def __str__(self):
        return f"First Name: {self.__first_name}\nLast Name: {self.__last_name}"

    def __repr__(self):
        return f"Person <{self.__last_name}, {self.__first_name}>"

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

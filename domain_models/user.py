import domain_models.person
import domain_models.movie
import domain_models.review
from datetime import datetime
import re
import phonenumbers
from password_validator import PasswordValidator


class User(Person):

    def __init__(self, first_name: str = None, last_name: str = None, email_address: str = None, password: str = "yourpasswordwasweakchangeit!", phone_number: str = None, gender: int = None, date_of_birth: datetime = datetime(1970, 1, 1), watchlist: list = [], watched_movies: list = [], reviews: list = []):

        # Parent Class Call
        super(first_name, last_name)

        # Email Address
        self.__email_address = email_address.strip() if self.__valid_email_address(
            email_address.strip()) else None

        # Password
        self.__password = password if self.__valid_password(
            password) else "yourpasswordwasweakchangeit!"

        # Phone Number
        self.__phone_number = phone_number if self.__valid_phone_number(
            phone_number) else None

        # Gender --> 1: Male, 2: Female, 3: Homosexual, 4: Bi-Sexual, 5: Other
        self.__gender = gender if gender in (1, 2, 3, 4, 5) else 1

        # Date of Birth
        try:
            self.__date_of_birth = datetime(date_of_birth)
        except Exception as e:
            print(f"Date of birth error: {e}")
            self.__date_of_birth = datetime(1970, 1, 1)

        # Watchlist
        self.__watchlist = watchlist if self.__valid_watchlist(
            watchlist) else self.__cleaned_watchlist()

        # Watched Movies
        self.__watched_movies = watched_movies if self.__valid_watch_movies(
            watched_movies) else self.__cleaned_watched_movies()

        # Reviews
        self.__reviews = reviews if self.__valid_reviews(
            reviews) else self.__cleaned_reviews()

    # Phone Number Check

    def __valid_phone_number(self, phone_number: str):
        # None means no specific country
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if phonenumbers.is_valid_number(parsed_number):
                return parsed_number
            else:
                return None
        except Exception as e:
            print(f'Phone Number Parsing Error: {e}')
            return None

    # Email Address Check
    def __valid_email_address(self, email_address: str) -> str:
        return (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email_address) != None)

    # Password Check
    def __valid_password(self, password: str) -> str:

        if type(password) == str:

            schema = PasswordValidator()

            schema\
                .min(8)\
                .max(100)\
                .has().uppercase()\
                .has().lowercase()\
                .has().digits()\
                .has().no().spaces()\
                .has().symbols()\

            return schema.validate(password)

        else:
            return False

    # Watchlist Check
    def __valid_watchlist(self, watchlist: list) -> list:
        for movie in watchlist:
            if isinstance(movie, Movie):
                return False
        return True

    # Watchlist Cleaner
    def __cleaned_watchlist(self, watchlist: list) -> list:

        cleaned_list = []

        for movie in watchlist:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

    # Watched Movies Check
    def __valid_watched_movies(self, watched_movies: list) -> list:
        for movie in watched_movies:
            if isinstance(movie, Movie):
                return False
        return True

    # Watched Movies Cleaner
    def __cleaned_watched_movies(self, watched_movies: list) -> list:

        cleaned_list = []

        for movie in watched_movies:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

    # Reviews Check
    def __valid_reviews(self, reviews: list) -> list:
        for review in reviews:
            if isinstance(review, Review):
                return False
        return True

    # Reviews Cleaner
    def __cleaned_reviews(self, reviews: list) -> list:

        cleaned_list = []

        for review in reviews:
            if isinstance(review, Review):
                cleaned_list.append(review)

        return cleaned_list

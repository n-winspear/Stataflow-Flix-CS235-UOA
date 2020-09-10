class Genre:
    def __init__(self, genre_name: str):

        # Genre Name
        self.__genre_name = genre_name.strip() if type(genre_name) == str else None

    def __str__(self):
        return f"Movie Title: {self.__title}\nRelease Year: {self.__release_year}\nRuntime: {self.__runtime_minutes} mins"

    def __repr__(self):
        return f"Movie <{self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return (self.__title == other.title) and (self.__directors == other.directors)

    def __hash__(self):
        return hash(f"{self.__titel}{self.__release_year}")

    # Properties
    @property
    def genre_name(self):
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, genre_name: str) -> str:
        self.__genre_name = genre_name.strip() if type(genre_name) == str else None

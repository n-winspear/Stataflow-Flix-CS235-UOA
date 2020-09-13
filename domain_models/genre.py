class Genre:
    def __init__(self, genre_name: str):

        # Genre Name
        self.__genre_name = genre_name.strip() if type(genre_name) == str else None

    def __str__(self):
        return f"Genre: {self.__genre_name}"

    def __repr__(self):
        return f"Genre <{self.genre_name}>"

    def __eq__(self, other):
        return (self.__genre_name == other.genre_name)

    def __hash__(self):
        return hash(f"{self.__genre_name}")

    # Properties
    @property
    def genre_name(self):
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, genre_name: str) -> str:
        self.__genre_name = genre_name.strip() if type(genre_name) == str else None

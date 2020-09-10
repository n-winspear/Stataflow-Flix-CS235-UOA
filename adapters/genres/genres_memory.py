from adapters.genres.genres_abstract import GenresAbstract
from domain_models.genre import Genre


class GenresMemory(GenresAbstract):

    # GET
    @abc.abstractmethod
    def get_genre(self, genre: Genre):
        matches = []

        for stored_genre in self.__genres:
            if genre == stored_genre:
                matches.append(stored_genre)
        return matches

    # INSERT
    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        if isinstance(genre, Genre):
            self.__genres.append(genre)

    # UPDATE
    @abc.abstractmethod
    def update_genre(self, genre: Genre, new_genre: Genre):

        genre_details = self.get_genre(genre)

        if genre_details.genre_name != new_genre.genre_name:
            genre_details.genre_name = new_genre.genre_name

    # DELETE
    @abc.abstractmethod
    def delete_genre(self, genre: Genre):
        for stored_genre in self.__genres:
            if genre == stored_genre:
                self.__actors.remove(genre)

    # GET ALL
    @abc.abstractmethod
    def get_all_genres(self):
        return self.__genres

    # INSERT MULTIPLE
    @abc.abstractmethod
    def insert_multiple_genres(self, genres: list):
        for genre in genres:
            if isinstance(genre, Genre):
                self.__genres.append(genre)

import abc


class GenresAbstract(abc.ABC):

    # GET
    @abc.abstractmethod
    def get_genre(self, genre: Genre):
        raise NotImplementedError

    # INSERT
    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    # UPDATE
    @abc.abstractmethod
    def update_genre(self, genre: Genre):
        raise NotImplementedError

    # DELETE
    @abc.abstractmethod
    def delete_genre(self, genre: Genre):
        raise NotImplementedError

    # GET ALL
    @abc.abstractmethod
    def get_all_genres(self):
        raise NotImplementedError

    # INSERT MULTIPLE
    @abc.abstractmethod
    def insert_multiple_genres(self, genres: list):
        raise NotImplementedError

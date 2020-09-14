from adapters.abstractrepository import AbstractRepository
from data_processors.moviecsvparser import MovieCSVParser
from domain_models.actor import Actor
from domain_models.director import Director
from domain_models.genre import Genre
from domain_models.movie import Movie
from domain_models.review import Review


class MemoryRepository(AbstractRepository):

    def __init__(self):
        file_path = 'data_processors/Data1000Movies.csv'
        fp = MovieCSVParser(file_path)
        fp.read_csv_file()

        self._dataset_of_actors = fp.dataset_of_actors
        self._dataset_of_movies = fp.dataset_of_movies
        self._dataset_of_directors = fp.dataset_of_directors
        self._dataset_of_genres = fp.dataset_of_genres
        self._dataset_of_reviews = fp.dataset_of_reviews

    ###############################################
    # Actor Methods
    ###############################################

   # GET
    def get_actor(self, actor: Actor):
        if isinstance(actor, Actor):
            matches = []
            for stored_actor in self._dataset_of_actors:
                if actor == stored_actor:
                    matches.append(stored_actor)
            if len(matches) > 0:
                return matches
            else:
                return None

    # INSERT
    def add_actor(self, actor: Actor):
        if isinstance(actor, Actor):
            self._dataset_of_actors.append(actor)

    # UPDATE
    def update_actor(self, actor: Actor, new_actor_details: Actor):
        if (isinstance(actor, Actor) and isinstance(new_actor_details, Actor)):

            actor_details = self.get_actor(actor)

            # Full Name Check
            if actor_details.full_name != new_actor_details.full_name:
                actor_details.full_name = new_actor_details.full_name

            # Gender Check
            if actor_details.gender != new_actor_details.gender:
                actor_details.gender = new_actor_details.gender

            # Date Of Birth Check
            if actor_details.date_of_birth != new_actor_details.date_of_birth:
                actor_details.date_of_birth = new_actor_details.date_of_birth

            # Movies Acted In Check
            if actor_details.movies_acted_in != new_actor_details.movies_acted_in:
                actor_details.movies_acted_in = new_actor_details.movies_acted_in

            # IMDB Page Check
            if actor_details.imdb_page != new_actor_details.imdb_page:
                actor_details.imdb_page = new_actor_details.imdb_page

    # DELETE
    def delete_actor(self, actor: Actor):
        if isinstance(actor, Actor):
            for stored_actor in self._dataset_of_actors:
                if actor == stored_actor:
                    self._dataset_of_actors.remove(stored_actor)

    # GET ALL
    def get_all_actors(self):
        return self._dataset_of_actors

    # INSERT MULTIPLE
    def insert_multiple_actors(self, actors: list):
        for actor in actors:
            if isinstance(actor, Actor) and actor not in self._dataset_of_actors:
                self._dataset_of_actors.append(actor)

    ###############################################
    # Director Methods
    ###############################################

    # GET
    def get_director(self, director: Director):
        if isinstance(director, Director):
            matches = []
            for stored_director in self._dataset_of_directors:
                if director == stored_director:
                    matches.append(stored_director)
            if len(matches) > 0:
                return matches
            else:
                return None

    # INSERT
    def add_director(self, director: Director):
        if isinstance(director, Director):
            self._dataset_of_directors.append(director)

    # UPDATE
    def update_director(self, director: Director, new_director_details: Director):
        if (isinstance(director, Director) and isinstance(new_director_details, Director)):

            director_details = self.get_director(director)

            # Full Name Check
            if director_details.full_name != new_director_details.full_name:
                director_details.full_name = new_director_details.full_name

            # Gender Check
            if director_details.gender != new_director_details.gender:
                director_details.gender = new_director_details.gender

            # Date Of Birth Check
            if director_details.date_of_birth != new_director_details.date_of_birth:
                director_details.date_of_birth = new_director_details.date_of_birth

            # Movies Acted In Check
            if director_details.movies_directed != new_director_details.movies_directed:
                director_details.movies_directed = new_director_details.movies_directed

            # IMDB Page Check
            if director_details.imdb_page != new_director_details.imdb_page:
                director_details.imdb_page = new_director_details.imdb_page

    # DELETE
    def delete_director(self, director: Director):
        if isinstance(director, Director):
            for stored_director in self._dataset_of_directors:
                if director == stored_director:
                    self._dataset_of_directors.remove(stored_director)

    # GET ALL
    def get_all_directors(self):
        return self._dataset_of_directors

    # INSERT MULTIPLE
    def insert_multiple_directors(self, directors: list):
        for director in directors:
            if isinstance(director, Director) and director not in self._dataset_of_directors:
                self._dataset_of_directors.append(director)

    ###############################################
    # Genre Methods
    ###############################################

    # GET
    def get_genre(self, genre: Genre):
        if isinstance(genre, Genre):
            matches = []
            for stored_genre in self._dataset_of_genres:
                if genre == stored_genre:
                    matches.append(stored_genre)
            if len(matches) > 0:
                return matches
            else:
                return None

    # INSERT
    def add_genre(self, genre: Genre):
        if isinstance(genre, Genre):
            self._dataset_of_genres.append(genre)

    # UPDATE
    def update_genre(self, genre: Genre, new_genre_details: Genre):
        if (isinstance(genre, Genre) and isinstance(new_genre_details, Genre)):

            genre_details = self.get_genre(genre)

            # Genre Name Check
            if genre_details.genre_name != new_genre_details.genre_name:
                genre_details.genre_name = new_genre_details.genre_name

    # DELETE
    def delete_genre(self, genre: Genre):
        if isinstance(genre, Genre):
            for stored_genre in self._dataset_of_genres:
                if genre == stored_genre:
                    self._dataset_of_genres.remove(stored_genre)

    # GET ALL
    def get_all_genres(self):
        return self._dataset_of_genres

    # INSERT MULTIPLE
    def insert_multiple_genres(self, genres: list):
        for genre in genres:
            if isinstance(genre, Genre) and genre not in self._dataset_of_genres:
                self._dataset_of_genres.append(genre)

    ###############################################
    # Movie Methods
    ###############################################

    # GET
    def get_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            matches = []
            for stored_movie in self._dataset_of_movies:
                if movie == stored_movie:
                    matches.append(stored_movie)
            if len(matches) > 0:
                return matches
            else:
                return None

    # INSERT
    def add_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            self._dataset_of_movies.append(movie)

    # UPDATE
    def update_movie(self, movie: Movie, new_movie_details: Movie):
        if (isinstance(movie, Movie) and isinstance(new_movie_details, Movie)):

            movie_details = self.get_movie(movie)

            # Movie Title Check
            if movie_details.title != new_movie_details.title:
                movie_details.title = new_movie_details.title

            # Movie Genre Check
            if movie_details.genre != new_movie_details.genre:
                movie_details.genre = new_movie_details.genre

            # Movie Description Check
            if movie_details.description != new_movie_details.description:
                movie_details.description = new_movie_details.description

            # Movie Directors Check
            if movie_details.directors != new_movie_details.directors:
                movie_details.directors = new_movie_details.directors

            # Movie Actors Check
            if movie_details.actors != new_movie_details.actors:
                movie_details.actors = new_movie_details.actors

            # Movie Runtime (Minutes) Check
            if movie_details.runtime_minutes != new_movie_details.runtime_minutes:
                movie_details.runtime_minutes = new_movie_details.runtime_minutes

            # Movie Average Rating Check
            if movie_details.average_rating != new_movie_details.average_rating:
                movie_details.average_rating = new_movie_details.average_rating

            # Movie Vote Count Check
            if movie_details.vote_count != new_movie_details.vote_count:
                movie_details.vote_count = new_movie_details.vote_count

            # Movie Revenue Check
            if movie_details.revenue != new_movie_details.revenue:
                movie_details.revenue = new_movie_details.revenue

            # Movie Metascore Check
            if movie_details.metascore != new_movie_details.metascore:
                movie_details.metascore = new_movie_details.metascore

    # DELETE

    def delete_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            for stored_movie in self._dataset_of_movies:
                if movie == stored_movie:
                    self._dataset_of_movies.remove(stored_movie)

    # GET ALL
    def get_all_movies(self):
        return self._dataset_of_movies

    # INSERT MULTIPLE
    def insert_multiple_movies(self, movies: list):
        for movie in movies:
            if isinstance(movie, Movie) and movie not in self._dataset_of_movies:
                self._dataset_of_movies.append(movie)

    ###############################################
    # Review Methods
    ###############################################

    # GET
    def get_review(self, review: Review):
        if isinstance(review, Review):
            matches = []
            for stored_review in self._dataset_of_reviews:
                if review == stored_review:
                    matches.append(stored_review)
            if len(matches) > 0:
                return matches
            else:
                return None

    # INSERT
    def add_review(self, review: Review):
        if isinstance(review, Review):
            self._dataset_of_reviews.append(review)

    # UPDATE
    def update_review(self, review: Review, new_review_details: Review):
        if (isinstance(review, Review) and isinstance(new_review_details, Review)):

            review_details = self.get_review(review)

            # Review Name Check
            if review_details.movie != new_review_details.movie:
                review_details.movie = new_review_details.movie

            # Review Name Check
            if review_details.rating != new_review_details.rating:
                review_details.rating = new_review_details.rating

            # Review Name Check
            if review_details.review_text != new_review_details.review_text:
                review_details.review_text = new_review_details.review_text

    # DELETE
    def delete_review(self, review: Review):
        if isinstance(review, Review):
            for stored_review in self._dataset_of_reviews:
                if review == stored_review:
                    self._dataset_of_reviews.remove(stored_review)

    # GET ALL
    def get_all_reviews(self):
        return self._dataset_of_reviews

    # INSERT MULTIPLE
    def insert_multiple_reviews(self, reviews: list):
        for review in reviews:
            if isinstance(review, Review) and review not in self._dataset_of_reviews:
                self._dataset_of_reviews.append(review)

    ###############################################
    # User Methods
    ###############################################

    # IMPLEMENT THESE

from backendflask.domain_models.movie import Movie
from backendflask.domain_models.genre import Genre
from backendflask.domain_models.director import Director
from backendflask.domain_models.actor import Actor
import pytest
import uuid
from datetime import datetime


@pytest.fixture
def empty_movie():
    return Movie(
        title='Harry Potter and the Prisoner of Azkaban',
    )


@pytest.fixture
def filled_movie():
    return Movie(
        title='The Shawshank Redemption',
        movieID='fb0e4da7-5152-4391-abcc-19ea8f4ad619',
        release_year=1994,
        genres=[Genre('Drama'), Genre('Thriller')],
        description='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        directors=[Director(full_name='Frank Darabont',
                            personID='863ede0e-9da6-4a3c-a76b-6ff8b18858d2')],
        actors=[Actor(full_name='Tim Robbins', personID='f7275e9a-6867-48f8-9730-f2c65214f325'), Actor(full_name='Morgan Freeman',
                                                                                                       personID='91bcd77a-96fc-4c65-b122-7ef7980475ba'), Actor(full_name='Bob Gunton', personID='1fa6485d-c1c3-4883-96ef-0367a592acd8')],
        runtime_minutes=142,
        average_rating=9.3,
        vote_count=2291675,
        revenue=28815291.0,
        metascore=80
    )


def test_empty_movie_initalisation(empty_movie):
    assert empty_movie.title == 'Harry Potter and the Prisoner of Azkaban'
    assert empty_movie.movieID.version == 4
    assert empty_movie.release_year == None
    assert empty_movie.genres == []
    assert empty_movie.description == None
    assert empty_movie.directors == []
    assert empty_movie.actors == []
    assert empty_movie.runtime_minutes == 0
    assert empty_movie.average_rating == 0.0
    assert empty_movie.vote_count == 0
    assert empty_movie.revenue == 0.0
    assert empty_movie.metascore == 0


def test_filled_movie_initialisation(filled_movie):
    assert filled_movie.title == 'The Shawshank Redemption'
    assert filled_movie.movieID == 'fb0e4da7-5152-4391-abcc-19ea8f4ad619'
    assert filled_movie.release_year == 1994
    assert filled_movie.genres == [Genre('Drama'), Genre('Thriller')]
    assert filled_movie.description == 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'
    assert filled_movie.directors == [Director(
        full_name='Frank Darabont', personID='863ede0e-9da6-4a3c-a76b-6ff8b18858d2')]
    assert filled_movie.actors == [Actor(full_name='Tim Robbins', personID='f7275e9a-6867-48f8-9730-f2c65214f325'), Actor(full_name='Morgan Freeman',
                                                                                                                          personID='91bcd77a-96fc-4c65-b122-7ef7980475ba'), Actor(full_name='Bob Gunton', personID='1fa6485d-c1c3-4883-96ef-0367a592acd8')]
    assert filled_movie.runtime_minutes == 142
    assert filled_movie.average_rating == 9.3
    assert filled_movie.vote_count == 2291675
    assert filled_movie.revenue == 28815291.0
    assert filled_movie.metascore == 80


def test_stringify_movie(filled_movie):
    assert str(
        filled_movie) == 'The Shawshank Redemption, 1994'


def test_representation_movie(filled_movie):
    assert repr(filled_movie) == 'Movie <The Shawshank Redemption, 1994>'


def test_equality_movie(filled_movie):
    assert filled_movie == Movie(title='The Shawshank Redemption', directors=[
                                 Director(full_name='Frank Darabont')])


def test_hash_movie(filled_movie):
    return hash(filled_movie) == hash(filled_movie)


def test_setters(empty_movie):
    empty_movie.title = 'Interstellar'
    empty_movie.release_year = 2014
    empty_movie.genres = [Genre('Adventure'), Genre('Drama'), Genre('Sci-Fi')]
    empty_movie.description = "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
    empty_movie.directors = [Director(
        full_name='Christopher Nolan')]
    empty_movie.actors = [Actor(full_name='Matthew McConaughey'), Actor(
        full_name='Anne Hathaway'), Actor(full_name='Jessica Chastain')]
    empty_movie.runtime_minutes = 169
    empty_movie.average_rating = 8.6
    empty_movie.vote_count = 1464716
    empty_movie.revenue = 696258169.0
    empty_movie.metascore = 74

    assert empty_movie.title == 'Interstellar'
    assert empty_movie.movieID.version == 4
    assert empty_movie.release_year == 2014
    assert empty_movie.genres == [
        Genre('Adventure'), Genre('Drama'), Genre('Sci-Fi')]
    assert empty_movie.description == "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
    assert empty_movie.directors == [Director(
        full_name='Christopher Nolan')]
    assert empty_movie.actors == [Actor(full_name='Matthew McConaughey'), Actor(
        full_name='Anne Hathaway'), Actor(full_name='Jessica Chastain')]
    assert empty_movie.runtime_minutes == 169
    assert empty_movie.average_rating == 8.6
    assert empty_movie.vote_count == 1464716
    assert empty_movie.revenue == 696258169.0
    assert empty_movie.metascore == 74


def test_actor_validator(empty_movie):
    empty_movie.actors = [Actor(full_name='Matthew McConaughey'), Actor(
        full_name='Anne Hathaway'), Actor(full_name='Jessica Chastain'), 'Tom Ellis', 'Rami Malek', 1542]
    assert empty_movie.actors == [Actor(full_name='Matthew McConaughey'), Actor(
        full_name='Anne Hathaway'), Actor(full_name='Jessica Chastain')]


def test_director_validator(empty_movie):
    empty_movie.directors = [Director(
        full_name='Christopher Nolan'), 'Taika Waititi', 8676]
    assert empty_movie.directors == [Director(
        full_name='Christopher Nolan')]


def test_genre_validator(empty_movie):
    empty_movie.genres = [Genre('Comedy'), Genre('Romance'), 'Drama', 5647]
    assert empty_movie.genres == [Genre('Comedy'), Genre('Romance')]


def test_release_year_validator(empty_movie):
    empty_movie.release_year = 1765
    assert empty_movie.release_year == None
    empty_movie.release_year = 2025
    assert empty_movie.release_year == None
    empty_movie.release_year = 2016
    assert empty_movie.release_year == 2016

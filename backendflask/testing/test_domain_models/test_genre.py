from backendflask.domain_models.genre import Genre
import pytest


@pytest.fixture
def empty_genre():
    return Genre(
        genre_name='Thriller',
    )


@pytest.fixture
def filled_genre():
    return Genre(
        genre_name='Comedy',
        genreID='36ebdb3c-ddf2-4936-a30f-cc079ea4f39c',
    )


def test_empty_genre_initalisation(empty_genre):
    assert empty_genre.genre_name == 'Thriller'
    assert empty_genre.genreID.version == 4


def test_filled_genre_initialisation(filled_genre):
    assert filled_genre.genre_name == 'Comedy'
    assert filled_genre.genreID == '36ebdb3c-ddf2-4936-a30f-cc079ea4f39c'


def test_stringify_genre(filled_genre):
    assert str(filled_genre) == 'Genre: Comedy'


def test_representation_genre(filled_genre):
    assert repr(filled_genre) == 'Genre <Comedy>'


def test_equality_genre(filled_genre):
    assert filled_genre == filled_genre


def test_hash_genre(filled_genre):
    assert hash(filled_genre) == hash(filled_genre)


def test_setters(empty_genre):
    empty_genre.genre_name = 'Romance'
    assert empty_genre.genre_name == 'Romance'

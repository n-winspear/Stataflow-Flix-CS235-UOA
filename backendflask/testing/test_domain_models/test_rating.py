from backendflask.domain_models.rating import Rating
from backendflask.domain_models.movie import Movie
import pytest


@pytest.fixture
def empty_rating():
    return Rating(
        movie=Movie('The Matrix')
    )


@pytest.fixture
def filled_rating():
    return Rating(
        movie=Movie('Inception'),
        ratingID='76f182ea-193a-45a3-8cb4-8ea9031dce1b',
        rating=7.2,
        userID='fee53459-3900-4718-be1d-4b8bc97c4be3'
    )


def test_empty_rating_initalisation(empty_rating):
    assert empty_rating.movie == Movie('The Matrix')
    assert empty_rating.ratingID.version == 4
    assert empty_rating.rating == None
    assert empty_rating.userID.version == 4


def test_filled_rating_initialisation(filled_rating):
    assert filled_rating.movie == Movie('Inception')
    assert filled_rating.ratingID == '76f182ea-193a-45a3-8cb4-8ea9031dce1b'
    assert filled_rating.rating == 7.2
    assert filled_rating.userID == 'fee53459-3900-4718-be1d-4b8bc97c4be3'


def test_stringify_rating(filled_rating):
    assert str(filled_rating) == 'Rating: 7.2'


def test_representation_rating(filled_rating):
    assert repr(filled_rating) == 'Rating <7.2>'


def test_equality_rating(filled_rating):
    assert filled_rating == filled_rating


def test_hash_rating(filled_rating):
    assert hash(filled_rating) == hash(filled_rating)


def test_setters(empty_rating):
    empty_rating.movie = Movie('Avengers: Endgame')
    empty_rating.rating = 8.5

    assert empty_rating.movie == Movie('Avengers: Endgame')
    assert empty_rating.rating == 8.5

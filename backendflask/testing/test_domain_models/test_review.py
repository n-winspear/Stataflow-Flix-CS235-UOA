from backendflask.domain_models.review import Review
from backendflask.domain_models.movie import Movie
import pytest


@pytest.fixture
def empty_review():
    return Review(
        movie=Movie('The Matrix')
    )


@pytest.fixture
def filled_review():
    return Review(
        movie=Movie('Inception'),
        reviewID='76f182ea-193a-45a3-8cb4-8ea9031dce1b',
        review_text='This is a super awesome review for this movie.',
        userID='fee53459-3900-4718-be1d-4b8bc97c4be3'
    )


def test_empty_review_initalisation(empty_review):
    assert empty_review.movie == Movie('The Matrix')
    assert empty_review.reviewID.version == 4
    assert empty_review.review_text == None
    assert empty_review.userID.version == 4


def test_filled_review_initialisation(filled_review):
    assert filled_review.movie == Movie('Inception')
    assert filled_review.reviewID == '76f182ea-193a-45a3-8cb4-8ea9031dce1b'
    assert filled_review.review_text == 'This is a super awesome review for this movie.'
    assert filled_review.userID == 'fee53459-3900-4718-be1d-4b8bc97c4be3'


def test_stringify_review(filled_review):
    assert str(
        filled_review) == 'This is a super awesome review for this movie.'


def test_representation_review(filled_review):
    assert repr(
        filled_review) == 'Review <Inception, None, This is a super awesome review for this movie.>'


def test_equality_review(filled_review):
    assert filled_review == filled_review


def test_hash_review(filled_review):
    assert hash(filled_review) == hash(filled_review)


def test_setters(empty_review):
    empty_review.movie = Movie('Avengers: Endgame')
    empty_review.review_text = 'This is an even better review for an even better movie.'

    assert empty_review.movie == Movie('Avengers: Endgame')
    assert empty_review.review_text == 'This is an even better review for an even better movie.'

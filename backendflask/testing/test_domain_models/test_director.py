from backendflask.domain_models.director import Director
import pytest
import uuid
from datetime import datetime


@pytest.fixture
def empty_director():
    return Director(
        full_name='Natalie Portman',
    )


@pytest.fixture
def filled_director():
    return Director(
        full_name='Edgar Wright',
        personID='36ebdb3c-ddf2-4936-a30f-cc079ea4f39c',
        gender=1,
        date_of_birth='18/04/1974',
        imdb_page='https://www.imdb.com/name/nm0942367/'
    )


def test_empty_director_initalisation(empty_director):
    assert empty_director.full_name == 'Natalie Portman'
    assert empty_director.personID.version == 4
    assert empty_director.gender == 1
    assert empty_director.date_of_birth == None
    assert empty_director.imdb_page == None


def test_filled_director_initialisation(filled_director):
    assert filled_director.full_name == 'Edgar Wright'
    assert filled_director.personID == '36ebdb3c-ddf2-4936-a30f-cc079ea4f39c'
    assert filled_director.gender == 1
    assert filled_director.date_of_birth == '1974-04-18'
    assert filled_director.imdb_page == 'https://www.imdb.com/name/nm0942367/'


def test_stringify_director(filled_director):
    assert str(filled_director) == 'Full Name: Edgar Wright'


def test_representation_director(filled_director):
    assert repr(filled_director) == 'Director <Edgar Wright>'


def test_equality_director(filled_director):
    assert filled_director == filled_director


def test_hash_director(filled_director):
    assert hash(filled_director) == hash(filled_director)


def test_setters(empty_director):
    empty_director.full_name = 'Steven Spielberg'
    empty_director.gender = 4
    empty_director.date_of_birth = '18/12/1946'
    empty_director.imdb_page = 'https://www.imdb.com/name/nm0000229/'
    assert empty_director.full_name == 'Steven Spielberg'
    assert empty_director.gender == 4
    assert empty_director.date_of_birth == '1946-12-18'
    assert empty_director.imdb_page == 'https://www.imdb.com/name/nm0000229/'


def test_date_of_birth_validator(filled_director):
    assert filled_director.date_of_birth == '1974-04-18'
    filled_director.date_of_birth = '15/07/1999'
    assert filled_director.date_of_birth == '1999-07-15'
    filled_director.date_of_birth = 15
    assert filled_director.date_of_birth == None
    filled_director.date_of_birth = '15/07/2025'
    assert filled_director.date_of_birth == None
    filled_director.date_of_birth = '15/07/1803'
    assert filled_director.date_of_birth == None


def test_imdb_validator(filled_director):
    assert filled_director.imdb_page == 'https://www.imdb.com/name/nm0942367/'
    filled_director.imdb_page = 'randomnonurlstring'
    assert filled_director.imdb_page == None

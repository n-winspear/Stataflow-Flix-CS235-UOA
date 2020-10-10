from backendflask.domain_models.actor import Actor
import pytest
import uuid
from datetime import datetime


@pytest.fixture
def empty_actor():
    return Actor(
        full_name='Rami Malek',
    )


@pytest.fixture
def filled_actor():
    return Actor(
        full_name='Sarah Hyland',
        personID='36ebdb3c-ddf2-4936-a30f-cc079ea4f39c',
        gender=2,
        date_of_birth='24/11/1990',
        imdb_page='https://www.imdb.com/name/nm0405103/'
    )


def test_empty_actor_initalisation(empty_actor):
    assert empty_actor.full_name == 'Rami Malek'
    assert empty_actor.personID.version == 4
    assert empty_actor.gender == 1
    assert empty_actor.date_of_birth == None
    assert empty_actor.imdb_page == None


def test_filled_actor_initialisation(filled_actor):
    assert filled_actor.full_name == 'Sarah Hyland'
    assert filled_actor.personID == '36ebdb3c-ddf2-4936-a30f-cc079ea4f39c'
    assert filled_actor.gender == 2
    assert filled_actor.date_of_birth == '1990-11-24'
    assert filled_actor.imdb_page == 'https://www.imdb.com/name/nm0405103/'


def test_stringify_actor(filled_actor):
    assert str(filled_actor) == 'Full Name: Sarah Hyland'


def test_representation_actor(filled_actor):
    assert repr(filled_actor) == 'Actor <Sarah Hyland>'


def test_equality_actor(filled_actor):
    assert filled_actor == filled_actor


def test_hash_actor(filled_actor):
    assert hash(filled_actor) == hash(filled_actor)


def test_setters(empty_actor):
    empty_actor.full_name = 'Lauren German'
    empty_actor.gender = 3
    empty_actor.date_of_birth = '19/11/1978'
    empty_actor.imdb_page = 'https://www.imdb.com/name/nm0314514'
    assert empty_actor.full_name == 'Lauren German'
    assert empty_actor.gender == 3
    assert empty_actor.date_of_birth == '1978-11-19'
    assert empty_actor.imdb_page == 'https://www.imdb.com/name/nm0314514'


def test_date_of_birth_validator(filled_actor):
    assert filled_actor.date_of_birth == '1990-11-24'
    filled_actor.date_of_birth = '15/07/1999'
    assert filled_actor.date_of_birth == '1999-07-15'
    filled_actor.date_of_birth = 15
    assert filled_actor.date_of_birth == None
    filled_actor.date_of_birth = '15/07/2025'
    assert filled_actor.date_of_birth == None
    filled_actor.date_of_birth = '15/07/1803'
    assert filled_actor.date_of_birth == None


def test_imdb_validator(filled_actor):
    assert filled_actor.imdb_page == 'https://www.imdb.com/name/nm0405103/'
    filled_actor.imdb_page = 'randomnonurlstring'
    assert filled_actor.imdb_page == None

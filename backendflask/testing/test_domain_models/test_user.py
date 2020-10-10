from backendflask.domain_models.user import User
from backendflask.domain_models.movie import Movie
from backendflask.domain_models.review import Review
import pytest


@pytest.fixture
def empty_user():
    return User(
        first_name='Lucifer',
        last_name='Morningstar'
    )


@pytest.fixture
def filled_user():
    return User(
        first_name='Nathan',
        last_name='Winspear',
        personID='cdfe102a-e7cd-4762-a9ee-14db943892a6',
        email_address='n.winspear1@gmail.com',
        password='nU34N!39Yk#z$wBTDe$k',
        phone_number='+6421856498',
        gender=1,
        date_of_birth='15/07/1999',
        watchlist=[Movie('Mr Robot'), Movie('American Sniper'),
                   Movie('Harry Potter and the Half Blood Prince')],
        watched_movies=[Movie('Hot Fuzz'), Movie('Inception'), Movie(
            'Love Actually'), Movie('Avengers: Endgame')],
        reviews=[Review(movie=Movie('Hot Fuzz'), reviewID='cc58b5cb-fd2c-4f42-9187-28557baf5213', review_text='This movie is hilarious, highly recommend watching it!', userID='78c9713d-dc7e-459b-b955-ef7cad454282'),
                 Review(movie=Movie('Interstellar'), reviewID='a70ab3f8-9d7d-4415-aa9c-9b11acceb8e5', review_text='This movie is hilarious, highly recommend watching it!', userID='78c9713d-dc7e-459b-b955-ef7cad454282')]
    )


def test_empty_user_initalisation(empty_user):
    assert empty_user.first_name == 'Lucifer'
    assert empty_user.last_name == 'Morningstart'
    assert empty_user.personID.version == 4
    assert empty_user.email_address == None
    assert empty_user.password == None
    assert empty_user.phone_number == None
    assert empty_user.gender == 1
    assert empty_user.date_of_birth == None
    assert empty_user.watchlist == []
    assert empty_user.watched_movies == []
    assert empty_user.reviews == []


def test_filled_user_initialisation(filled_user):
    assert filled_user.first_name == 'Nathan'
    assert filled_user.last_name == 'Winspear'
    assert filled_user.personID == 'cdfe102a-e7cd-4762-a9ee-14db943892a6'
    assert filled_user.email_address == 'n.winspear1@gmail.com'
    assert filled_user.password == 'nU34N!39Yk#z$wBTDe$k'
    assert filled_user.phone_number == '+6421856498'
    assert filled_user.gender == 1
    assert filled_user.date_of_birth == '15/07/1999'
    assert filled_user.watchlist == [Movie('Mr Robot'), Movie('American Sniper'),
                                     Movie('Harry Potter and the Half Blood Prince')]
    assert filled_user.watched_movies == [Movie('Hot Fuzz'), Movie('Inception'), Movie(
        'Love Actually'), Movie('Avengers: Endgame')]
    assert filled_user.reviews == [Review(movie=Movie('Hot Fuzz'), reviewID='cc58b5cb-fd2c-4f42-9187-28557baf5213', review_text='This movie is hilarious, highly recommend watching it!', userID='78c9713d-dc7e-459b-b955-ef7cad454282'),
                                   Review(movie=Movie('Interstellar'), reviewID='a70ab3f8-9d7d-4415-aa9c-9b11acceb8e5', review_text='This movie is hilarious, highly recommend watching it!', userID='78c9713d-dc7e-459b-b955-ef7cad454282')]


def test_stringify_user(filled_user):
    assert str(filled_user) == 'Nathan Winspear'


def test_representation_user(filled_user):
    assert repr(filled_user) == 'User <Winspear, Nathan>'


def test_equality_user(filled_user):
    assert filled_user == filled_user


def test_hash_user(filled_user):
    assert hash(filled_user) == hash(filled_user)


def test_setters(empty_user):
    empty_user.first_name = 'Haley'
    empty_user.last_name = 'Dunphy'
    empty_user.email_address = 'h.dunphy@modernfamily.com'
    empty_user.password = '39enSma4Xb!lPu7eKwmm'
    empty_user.phone_number = '+6427648653'
    empty_user.gender = 2
    empty_user.date_of_birth = '16/01/1962'
    empty_user.watchlist = [Movie('Iron Man'), Movie('Mission Impossible'),
                            Movie('Kingsman the Secret Service')]
    empty_user.watched_movies = [Movie('The Hunger Games'), Movie('Grown Ups'), Movie(
        'The Fast and the Furious'), Movie('This is 40')]
    empty_user.reviews = [Review(movie=Movie('Iron Man'), reviewID='cc58b5cb-fd2c-4f42-9187-28557baf5213', review_text='This movie is a thrill ride, highly recommend watching it!', userID='78c9713d-dc7e-459b-b955-ef7cad454282'),
                          Review(movie=Movie('Fantastic Beasts and Where to Find Them'), reviewID='a70ab3f8-9d7d-4415-aa9c-9b11acceb8e5',
                                 review_text='Great extension to the Harry Potter universe', userID='78c9713d-dc7e-459b-b9empty_user')]

    assert empty_user.first_name == 'Haley'
    assert empty_user.last_name == 'Dunphy'
    assert empty_user.email_address == 'h.dunphy@modernfamily.com'
    assert empty_user.password == '39enSma4Xb!lPu7eKwmm'
    assert empty_user.phone_number == '+6427648653'
    assert empty_user.gender == 2
    assert empty_user.date_of_birth == '16/01/1962'
    assert empty_user.watchlist == [Movie('Iron Man'), Movie('Mission Impossible'),
                                    Movie('Kingsman the Secret Service')]
    assert empty_user.watched_movies == [Movie('The Hunger Games'), Movie('Grown Ups'), Movie(
        'The Fast and the Furious'), Movie('This is 40')]
    assert empty_user.reviews == [Review(movie=Movie('Iron Man'), reviewID='cc58b5cb-fd2c-4f42-9187-28557baf5213', review_text='This movie is a thrill ride, highly recommend watching it!', userID='78c9713d-dc7e-459b-b955-ef7cad454282'),
                                  Review(movie=Movie('Fantastic Beasts and Where to Find Them'), reviewID='a70ab3f8-9d7d-4415-aa9c-9b11acceb8e5',
                                         review_text='Great extension to the Harry Potter universe', userID='78c9713d-dc7e-459b-b9empty_user')]

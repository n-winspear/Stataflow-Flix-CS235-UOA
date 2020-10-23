from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.domain_models.actor import Actor
from backendflask.domain_models.director import Director
from backendflask.domain_models.genre import Genre
from backendflask.domain_models.movie import Movie
from backendflask.domain_models.review import Review
from backendflask.domain_models.rating import Rating
from backendflask.domain_models.user import User
import random
import pytest


@pytest.fixture
def memory_repository():
    return MemoryRepository()


def test_actor_dataset(memory_repository):
    length = len(memory_repository.get_all_actors())
    actor = Actor(
        full_name='Elliot Alderson', personID='2d7b1fc6-81d0-4bf0-953d-16ac283dad96')

    # Add Actor
    memory_repository.add_actor(actor)
    assert len(memory_repository.get_all_actors()) > length
    length += 1

    # Update Actor
    actor.full_name = 'Nathan Winspear'
    memory_repository.update_actor(actor)
    actor = memory_repository.get_actor(actor.personID)
    assert actor.full_name == 'Nathan Winspear'

    # Delete Actor
    memory_repository.delete_actor(actor.personID)
    assert len(memory_repository.get_all_actors()) < length
    length -= 1


def test_director_dataset(memory_repository):
    length = len(memory_repository.get_all_directors())
    director = Director(
        full_name='Edgar Wright', personID='1ae6a04a-63a4-42d7-b670-561212c6fb6c')

    # Add Director
    memory_repository.add_director(director)
    assert len(memory_repository.get_all_directors()) > length
    length += 1

    # Update Director
    director.full_name = 'Ella Lopez'
    memory_repository.update_director(director)
    director = memory_repository.get_director(director.personID)
    assert director.full_name == 'Ella Lopez'

    # Delete Director
    memory_repository.delete_director(director.personID)
    assert len(memory_repository.get_all_directors()) < length
    length -= 1


def test_genre_dataset(memory_repository):
    length = len(memory_repository.get_all_genres())
    genre = Genre(
        genre_name='New Genre', genreID='3cf38e43-f86b-4950-a5cb-588ac964671f')

    # Add Genre
    memory_repository.add_genre(genre)
    assert len(memory_repository.get_all_genres()) > length
    length += 1

    # Update Genre
    genre.genre_name = 'Updated Genre'
    memory_repository.update_genre(genre)
    genre = memory_repository.get_genre(genre.genreID)
    assert genre.genre_name == 'Updated Genre'

    # Delete Genre
    memory_repository.delete_genre(genre.genreID)
    assert len(memory_repository.get_all_genres()) < length
    length -= 1


def test_movie_dataset(memory_repository):
    length = len(memory_repository.get_all_movies())
    movie = Movie(
        title='A Million Ways to Die in the West', movieID='3cf38e43-f86b-4950-a5cb-588ac964671f')

    # Add Movie
    memory_repository.add_movie(movie)
    assert len(memory_repository.get_all_movies()) > length
    length += 1

    # Update Movie
    movie.title = 'Sherlock Holmes'
    memory_repository.update_movie(movie)
    movie = memory_repository.get_movie(movie.movieID)
    assert movie.title == 'Sherlock Holmes'

    # Delete Movie
    memory_repository.delete_movie(movie.movieID)
    assert len(memory_repository.get_all_movies()) < length
    length -= 1


def test_review_dataset(memory_repository):
    length = len(memory_repository.get_all_reviews())
    review = Review(movie=Movie('A Million Ways to Die in the West'),
                    review_text='This is a great movie!', reviewID='3cf38e43-f86b-4950-a5cb-588ac964671f')

    # Add Review
    memory_repository.add_review(review)
    assert len(memory_repository.get_all_reviews()) > length
    length += 1

    # Update Review
    review.review_text = 'This is a good movie!'
    memory_repository.update_review(review)
    review = memory_repository.get_review(review.reviewID)
    assert review.review_text == 'This is a good movie!'

    # Delete Review
    memory_repository.delete_review(review.reviewID)
    assert len(memory_repository.get_all_reviews()) < length
    length -= 1


def test_rating_dataset(memory_repository):
    length = len(memory_repository.get_all_ratings())
    rating = Rating(movie=Movie('A Million Ways to Die in the West'),
                    rating=6.3, ratingID='3cf38e43-f86b-4950-a5cb-588ac964671f')

    # Add Rating
    memory_repository.add_rating(rating)
    assert len(memory_repository.get_all_ratings()) > length
    length += 1

    # Update Rating
    rating.rating = 7.5
    memory_repository.update_rating(rating)
    rating = memory_repository.get_rating(rating.ratingID)
    assert rating.rating == 7.5

    # Delete Rating
    memory_repository.delete_rating(rating.ratingID)
    assert len(memory_repository.get_all_ratings()) < length
    length -= 1


def test_user_dataset(memory_repository):
    length = len(memory_repository.get_all_users())
    user = User(
        first_name='Elliot', last_name='Alderson', personID='3cf38e43-f86b-4950-a5cb-588ac964671f', email_address='n.winspear@leadership.ac.nz')

    # Add User
    memory_repository.add_user(user)
    assert len(memory_repository.get_all_users()) > length
    length += 1

    # Update User
    user.full_name = 'Sarah Hyland'
    memory_repository.update_user(user)
    user = memory_repository.get_user(user.email_address)
    assert user.full_name == 'Sarah Hyland'

    # Delete User
    memory_repository.delete_user(user.personID)
    assert len(memory_repository.get_all_users()) < length
    length -= 1

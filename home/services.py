from adapters.memoryrepository import MemoryRepository

repo = MemoryRepository()


def get_home_data():
    response = {
        "movies": [

        ],
        "reviews": [

        ]
    }

    movies = repo.get_all_movies()
    reviews = repo.get_all_reviews()

    for movie in movies:
        response['movies'].append({movie.title: {
            "release_year": movie.release_year,
            "genres": movie.genres,
            "description": movie.description,
            "directors": movie.directors,
            "actors": movie.actors,
            "runtime_minutes": movie.runtime_minutes,
            "average_rating": movie.average_rating,
            "vote_count": movie.vote_count,
            "revenue": movie.revenue,
            "metascore": movie.metascore
        }})

    for review in reviews:
        response['reviews'].append({review.movie: {
            "rating": review.rating,
            "review_text": review.review_text
        }})

    return response

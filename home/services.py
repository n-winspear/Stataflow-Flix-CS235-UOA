from adapters.memoryrepository import MemoryRepository

repo = MemoryRepository()


def get_home_data():
    response = {
        "movies": repo.get_all_movies(),
    }

    return response

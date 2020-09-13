from data_processors.moviecsvparser import MovieCSVParser

file_path = 'data_processors/Data1000Movies.csv'

fp = MovieCSVParser(file_name=file_path)
fp.read_csv_file()

print(f"{fp.dataset_of_movies}\n{fp.dataset_of_reviews}\n{fp.dataset_of_genres}\n{fp.dataset_of_directors}\n{fp.dataset_of_actors}")

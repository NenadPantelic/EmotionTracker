# file paths
# NOTE: make sure these files are placed in data folder
CSV_DATASET_FILE_PATH = "data/movies.csv"
DB_FILE_PATH = "data/movie.db"
IMDB_BASE_URL = "https://www.imdb.com/title/"

CSV_MOVIE_COLUMNS = set(["title", "director", "actors", "year", "duration", "avg_vote", "language",
                         "description", "production_company"])

# emotion JSON maps paths
IMPROVE_EMOTIONS_MAP_PATH = "data/emotions_map_improve.json"
KEEPUP_EMOTIONS_MAP_PATH = "data/emotions_map_keep_up.json"

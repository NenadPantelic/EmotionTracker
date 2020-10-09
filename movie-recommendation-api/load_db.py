import csv
from db.db_context import DbContext
from config import DB_FILE_PATH, CSV_DATASET_FILE_PATH, CSV_MOVIE_COLUMNS
from repository.movie_repository import MovieRepository
from repository.genre_repository import GenreRepository
from repository.movie_genre_repository import MovieGenreRepository

context = DbContext(DB_FILE_PATH)
if context.isConnectionOpened:
    movie_repo = MovieRepository(context)
    genre_repo = GenreRepository(context)
    movie_genre_repo = MovieGenreRepository(context)
    print("Creating tables....")
    # create tables
    context.execute_sql_command("CREATE TABLE IF NOT EXISTS genre(genre_id BIGINT(4) PRIMARY KEY NOT NULL, "
                              "genre_name VARCHAR (32) UNIQUE NOT NULL)")

    # TODO: recompose this table - actor table, director table, languages and connect them with m2m tables
    context.execute_sql_command("CREATE TABLE IF NOT EXISTS movie(movie_id VARCHAR(16) PRIMARY KEY NOT NULL, "
                              "title VARCHAR (50) NOT NULL,directors VARCHAR(255), actors VARCHAR(255), year INT(4), "
                              "duration INT(4),avg_vote DECIMAL(2,1), languages VARCHAR(64), description TEXT,"
                              "production_company VARCHAR(64), poster_url VARCHAR(512) DEFAULT NULL)")
    context.execute_sql_command("CREATE TABLE IF NOT EXISTS movie_genre(movie_id VARCHAR(16) REFERENCES movie (movie_id) "
                              "ON DELETE CASCADE ON UPDATE CASCADE,  genre_id  BIGINT (10) REFERENCES genre (genre_id) "
                              "ON DELETE CASCADE ON UPDATE CASCADE, PRIMARY KEY (movie_id, genre_id))")

    print("Tables created successfully.")

    print("Load data into database.This may take some time.")
    movies = []
    last_inserted_id = 0
    inserted_genres = {} # NOTE: if this script is used when there are already some genres present in the database, those
    # genres neet to be fetched from the db
    counter = 0
    with open(CSV_DATASET_FILE_PATH, "r") as data:
        dr = csv.DictReader(data)  # comma is default delimiter
        for row in dr:
            imdb_id = row["imdb_title_id"]
            db_values = [imdb_id]
            db_values.extend([row[col] for col in row if col in CSV_MOVIE_COLUMNS])
            db_values.append(None)
            print("Data loading....")#, end=" ")
            movie_id = movie_repo.add_movie(db_values)
            if movie_id is None:
                print(f"Warning! Movie  with the imdb id =[{imdb_id}] was not inserted!")
            genres = row["genre"]
            for genre in genres.split(","):
                if genre not in inserted_genres:
                    if last_inserted_id is None:
                        last_inserted_id = counter
                    last_inserted_id = genre_repo.add_genre((last_inserted_id + 1, genre))
                    genre_id = last_inserted_id
                    if genre_id is not None:
                        inserted_genres[genre] = genre_id
                        counter += 1
                    else:
                        print(f"Warning! Genre  with the name=[{genre}] was not inserted!")
                else:
                    genre_id = inserted_genres[genre]
                if movie_id is not None and genre_id is not None:
                    movie_genre_repo.add_movie_genre((movie_id, genre_id))
    print("Data successfully loaded into database.")
    context.close()
else:
    print("There is a problem with the database connection. Check database connection string!")

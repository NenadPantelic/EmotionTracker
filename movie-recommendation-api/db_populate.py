import csv
from db.db_utils import open_connection, execute_sql_command
from config import DB_FILE_PATH, CSV_DATASET_FILE_PATH, CSV_MOVIE_COLUMNS

conn = open_connection(DB_FILE_PATH)
if conn is not None:
    print("Creating tables....")
    # create tables
    execute_sql_command(conn, "CREATE TABLE IF NOT EXISTS genre(genre_id BIGINT(4) PRIMARY KEY NOT NULL, "
                              "genre_name VARCHAR (32) UNIQUE NOT NULL)")

    # TODO: recompose this table - actor table, director table, languages and connect them with m2m tables
    execute_sql_command(conn, "CREATE TABLE IF NOT EXISTS movie(movie_id VARCHAR(16) PRIMARY KEY NOT NULL, "
                              "title VARCHAR (50) NOT NULL,directors VARCHAR(255), actors VARCHAR(255), year INT(4), "
                              "duration INT(4),avg_vote DECIMAL(2,1), languages VARCHAR(64), description TEXT,"
                              "production_company VARCHAR(64), poster_url VARCHAR(512) DEFAULT NULL)")
    execute_sql_command(conn, "CREATE TABLE IF NOT EXISTS movie_genre(movie_id VARCHAR(16) REFERENCES movie (movie_id) "
                              "ON DELETE CASCADE ON UPDATE CASCADE,  genre_id  BIGINT (10) REFERENCES genre (genre_id) "
                              "ON DELETE CASCADE ON UPDATE CASCADE, PRIMARY KEY (movie_id, genre_id))")

    print("Tables created successfully")
    conn.close()
else:
    print("There is a problem with the database connection. Check database connection string!")

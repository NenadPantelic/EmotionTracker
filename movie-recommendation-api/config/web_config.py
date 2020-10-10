class Config:
    DEBUG = False
    TESTING = True
    SECRET_KEY = "%BFM(B78tKY7{ne>{.gb7=PS"

    # Server settings
    DB_SERVER = "localhost"
    SERVER_NAME = "localhost:8000"

    # SQL Alchemy setup
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/movie.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DATABASE_URI = "sqlite:///data/movie.db"


class StageConfig(Config):
    DB_SERVER = "xxx.xxx.xxx.xxx"
    DEBUG = False
    TESTING = False

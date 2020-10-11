from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from flask import Flask, jsonify, abort, request, make_response
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from repository.movie_repository import MovieRepository
from services.movie_recommendation_service import MovieRecommendationService
from config.web_config import Config
from flask_cors import cross_origin

app = Flask(__name__)
api = Api(app)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)

app.config.from_object("config.web_config.Config")
db_orm = SQLAlchemy(app)
recommender = MovieRecommendationService(db_orm)


class Movie(Base, db_orm.Model):
    __table__ = Base.metadata.tables['movie']


class Genre(Base, db_orm.Model):
    __table__ = Base.metadata.tables['genre']


class MovieGenre(Base, db_orm.Model):
    __table__ = Base.metadata.tables['movie_genre']


# move to the separate file
emotion_post_args = reqparse.RequestParser()
emotion_post_args.add_argument("emotion", type=str, help="Emotion which is used to recommend the movie",
                               required=True)
emotion_post_args.add_argument("num_of_movies", type=int, help="Number of movies to fetch.", required=True)
emotion_post_args.add_argument("recommendation_type", type=int, help="Type of recommendation.", required=True)


@app.route('/api/v1/recommend', methods=['POST'])
# TODO: left only for demo - configure CORS for future use
@cross_origin()
def recommend():
    if not request.json:
        response = make_response(jsonify(message="Bad request"), 400)
        abort(response)
    emotion = request.json.get("emotion", None)
    num_of_movies = request.json.get("num_of_movies", None)
    recommendation_type = request.json.get("recommendation_type", None)
    if emotion is None or num_of_movies is None or recommendation_type is None:
        response = make_response(jsonify(message="Request body is not valid."), 400)
        abort(response)
    output = recommender.recommend(emotion, recommendation_type, num_of_movies)
    status_code = output.get("status_code", 200)
    return jsonify(output), status_code


if __name__ == "__main__":
    app.run()

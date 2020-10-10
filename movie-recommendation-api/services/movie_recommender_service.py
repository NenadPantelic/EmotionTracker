from .recommender_service import RecommenderService
from exceptions.bad_parameters_exception import  BadParametersException
from exceptions.db_exception import DbException
from dto.movie_response import MovieResponse
from dto.error_response import ErrorResponse
from utils.poster_scraper import scrape_imdb_poster

class MovieRecommenderService(RecommenderService):
    def __init__(self, db_context, emo_improve_map, emo_keepup_map):
        self._db_context = db_context
        # TODO: find some reasonable mapping between emotions and movie genres
        self.emotion_improve_map = { "Angry" : "Comedy",
                                    "Disguist" : "",
                                    "Fear" : "",
                                    "Happy" : "",
                                    "Sad" : "",
                                    "Surprise" :"",
                                    "Neutral": ""}
        self.emotion_keepup_map = {}

    @property
    def db_context(self):
        return self._db_context

    # NOTE: unused
    def find_strongest_emotion(self, emotions):
        """
        Find the strongest emotion among all listed.
        :param emotions: emotions dictionary -> emotion:emotion value
        :return:
        """
        return max(emotions, key=lambda entry:entry[1])

    def map_emotion_to_genre(self, emotion, recommendation_type="improve"):
        """
        Maps emotion to specific movie genre.
        :param emotion: emotion that should determine genre of movie that will be recommended
        :param recommendation_type: improve or keep up
        :return: genre of movie
        """
        if recommendation_type not in ("improve", "keepup"):
            raise BadParametersException(f"Recommendation type = {recommendation_type} is not valid.")
        if emotion not in self.emotion_improve_map and emotion not in self.emotion_keepup_map:
            raise BadParametersException(f"Emotion  value = {emotion} is not valid.")
        return self.emotion_improve_map[emotion] if recommendation_type == "improve" \
            else self.emotion_keepup_map

    # TODO: refactor note - create controller - service - dao flow
    def find_best_movies_by_genre(self, genre, num_of_movies=5):
        # TODO: use cache
        query = '''SELECT movie.movie_id, title, directors, actors, duration, avg_vote, poster_url, year, 
                   production_company, genre_name FROM (SELECT * FROM movie_genre INNER JOIN genre ON genre.genre_id= 
                   movie_genre.genre_id WHERE genre_name =:genre_name) AS MG INNER JOIN movie ON 
                   MG.movie_id = movie.movie_id ORDER BY avg_vote DESC LIMIT :num_of_movies'''
        return  self.db_context.session.execute(query,
                        {"genre_name": genre, "num_of_movies": num_of_movies}).fetchall()

    def find_movie_url(self, movie_id):
        return scrape_imdb_poster(movie_id)


    def recommend(self, emotion, recommendation_type = "improve", num_of_movies=10):
        """
        Recommends best movies based on provided emotions.
        :param emotions: dictionary of emotions
        :param recommendation_type: improve or keep up
        :param num_of_movies: positive number of movies to recommend
        :return: list of movies
        """
        if num_of_movies <= 0:
            raise BadParametersException("Number of movies to recommend must be positive.")
        #strongest_emotion = self.find_strongest_emotion(emotions)
        recommended_genre = self.map_emotion_to_genre(emotion, recommendation_type)
        try:
            movies = self.find_best_movies_by_genre(recommended_genre, num_of_movies)
            movie_details = []
            for movie in movies:
                movie_dto = MovieResponse(*movie).as_json()
                movie_dto["poster_url"] = self.find_movie_url(movie_dto["imdb_url"])
                movie_details.append(movie_dto)
            return {"movies":movie_details}
        except Exception as e:
            return error_response(e.message)







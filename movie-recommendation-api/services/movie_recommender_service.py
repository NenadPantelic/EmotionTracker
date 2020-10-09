from .recommender_service import RecommenderService
from exceptions.bad_parameters_exception import  BadParametersException

class MovieRecommenderService(RecommenderService):
    def __init__(self, movie_repo, emo_improve_map, emo_keepup_map):
        self.movie_repo = movie_repo
        # TODO: find some reasonable mapping between emotions and movie genres
        self.emotion_improve_map = { "Angry" : "Comedy",
                                    "Disguist" : "",
                                    "Fear" : "",
                                    "Happy" : "",
                                    "Sad" : "",
                                    "Surprise" :"",
                                    "Neutral": ""}
        self.emotion_keepup_map = {}

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


    def recommend(self, emotions, recommendation_type = "improve", num_of_movies=10):
        """
        Recommends best movies based on provided emotions.
        :param emotions: dictionary of emotions
        :param recommendation_type: improve or keep up
        :param num_of_movies: positive number of movies to recommend
        :return: list of movies
        """
        if num_of_movies <= 0:
            raise BadParametersException("Number of movies to recommend must be positive.")
        strongest_emotion = self.find_strongest_emotion(emotions)
        recommended_genre = self.map_emotion_to_genre(strongest_emotion, recommendation_type)
        return self.movie_repo.find_best_movies_by_genre(recommended_genre, num_of_movies)






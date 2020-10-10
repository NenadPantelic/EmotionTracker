from config.config import IMDB_BASE_URL


class MovieResponse:
    # TODO: refactor this - use named parameters
    def __init__(self, *vargs):
        self.movie_id = vargs[0]
        self.imdb_url = IMDB_BASE_URL + self.movie_id + "/"
        self.title = vargs[1]
        self.directors = vargs[2]
        self.actors = vargs[3]
        self.duration = vargs[4]
        self.score = vargs[5]
        self.poster_url = vargs[6]
        self.year = vargs[7]
        self.production_company = vargs[8]
        self.genre_name = vargs[9]

    def as_json(self):
        return self.__dict__ if self else {}

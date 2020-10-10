class Movie:
    def __init__(self, movie_id, title, directors, actors, duration, avg_vote, poster_url, year,
                 production_company):
        self._movie_id = movie_id
        self._title = title
        self._directors = directors
        self._actors = actors
        self._duration = duration
        self._year = year
        self._score = avg_vote
        self._poster_url = poster_url
        self._imdb_url = "https://www.imdb.com/title/" + self._movie_id + "/"
        self._production_company = production_company

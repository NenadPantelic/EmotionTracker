from .base_repository import IRepository


class MovieRepository(IRepository):
    def __init__(self, context):
        super().__init__(context)

    def add_movie(self, movie):
        """
            Creates a new movie into the movie table
            movie: movie params tuple
            :return: movie id
            """
        command = ''' INSERT INTO movie(movie_id, title, year, duration, languages, directors, production_company, 
                    actors, description, avg_vote, poster_url) VALUES(?,?,?,?,?, ?,?,?,?,?,?) '''
        new_id = super().add(command, movie)
        return new_id

    def findall(self):
        return super()._findall("movie")





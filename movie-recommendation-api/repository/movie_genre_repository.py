from .base_repository import IRepository


class MovieGenreRepository(IRepository):
    def __init__(self, context):
        super().__init__(context)

    def add_movie_genre(self, movie_genre):
        """
            Creates a new movie into the movie table
            movie: movie params tuple
            :return: movie id
            """
        command = ''' INSERT INTO movie_genre(movie_id, genre_id) VALUES(?,?) '''
        new_id = super().add(command, movie_genre)
        return new_id

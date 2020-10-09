from .base_repository import IRepository


class GenreRepository(IRepository):
    def __init__(self, context):
        super().__init__(context)

    def add_genre(self, genre):
        """
                Creates a new movie into the movie table
                movie: movie params tuple
                :return: movie id
                """
        command = ''' INSERT INTO genre(genre_id,genre_name) VALUES(?,?) '''
        return super().add(command, genre)

    def findall(self):
        return super()._findall("genre")

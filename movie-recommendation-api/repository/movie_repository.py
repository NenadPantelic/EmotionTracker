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
                    actors, description, avg_vote, poster_url) VALUES(?,?,?,?, ?,?, ?,?, ?,?, ?) '''
        new_id = super().add(command, movie)
        return new_id

    def findall(self):
        return super()._findall("movie")

    def find_best_scored_movies(self, num_of_movies):
        pass

    def find_best_movies_by_genre(self, genre, num_of_movies=5):
        # need to be cached
        query = '''SELECT movie.movie_id, title, directors, actors, duration, avg_vote, poster_url, year, 
                   production_company  FROM (SELECT * FROM movie_genre INNER JOIN genre ON genre.genre_id= 
                   movie_genre.genre_id WHERE genre_name =?) AS MG INNER JOIN movie ON 
                   MG.movie_id = movie.movie_id ORDER BY avg_vote DESC LIMIT ?'''
        movie_list = super()._find(query, (genre, num_of_movies))
        return movie_list



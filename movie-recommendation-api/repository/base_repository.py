from exceptions.db_exception import DbException
class IRepository:
    def __init__(self, context):
        self._context = context

    def add(self, sql_ddl, args):
        """
            Creates a new movie into the movie table
            movie: movie params tuple
            :return: movie id
            """
        try:
            cursor = self._context.execute_sql_command(sql_ddl, args=args)
            last_id = cursor.lastrowid
        except DbException as e: # log this message
            last_id = None
        return last_id

    def _findall(self, entity):
        query = ''f'SELECT * from {entity}'''
        try:
            cursor = self._context.execute_sql_command(query)
            return cursor.fetchall()
        except DbException as e:  # log this message
            print("Some error occurred during data fetching.")
            return None

    def _find(self, query, params):
        try:
            cursor = self._context.execute_sql_command(query, args=params)
            return cursor.fetchall()
        except DbException as e: # log this message
            print("Some error occurred during data fetching.")
            return None


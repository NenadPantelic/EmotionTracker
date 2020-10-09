from sqlite3 import connect, Error


class DbContext:

    def __init__(self, db_connection):
        self._conn = self.open_connection(db_connection)

    @property
    def conn(self):
        return self._conn

    def open_connection(self, db_connection):
        """ creates a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = connect(db_connection)
        except Error as e:
            print(e)

        return conn

    def isConnectionOpened(self):
        return self.conn is not None

    def execute_sql_command(self, command, require_commit=True):
        """
        Executes custom SQL command.
        :param conn: connection object
        :param command: SQL command that should be executed
        :param require_commit: does the command require commit
        :return: cursor object
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(command)
            if require_commit:
                self.conn.commit()
        except Error:
            print(
                "Some error occurred during db commit. Check your command parameters and db settings.")  # TODO: use logger
        return cursor


    def close(self):
        if self.conn:
            self.conn.close()

from sqlite3 import connect, Error


def open_connection(db_file):
    """ creates a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)

    return conn


def execute_sql_command(conn, command, require_commit=True):
    """
    Executes custom SQL command.
    :param conn: connection object
    :param command: SQL command that should be executed
    :param require_commit: does the command require commit
    :return: cursor object
    """
    cursor = conn.cursor()
    cursor.execute(command)
    if require_commit:
        conn.commit()
    return cursor

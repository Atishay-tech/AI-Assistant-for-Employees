import mysql.connector as mysql

class UseDatabase:

    def __init__(self, dbconfig: dict) -> None:
        self.config = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, type, value, traceback) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
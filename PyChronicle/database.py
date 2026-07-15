import sqlite3
import json
from datetime import datetime


class DatabaseManager:

    def __init__(self, db_name="history.db"):

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.create_table()


    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS execution_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            filename TEXT,

            function_name TEXT,

            line_number INTEGER,

            variables TEXT

        )
        """)

        self.connection.commit()



    def save_execution(self,
                       filename,
                       function_name,
                       line_number,
                       variables):

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute("""

        INSERT INTO execution_history(

            timestamp,

            filename,

            function_name,

            line_number,

            variables

        )

        VALUES(?,?,?,?,?)

        """,

        (

            current_time,

            filename,

            function_name,

            line_number,

            json.dumps(variables, default=str)

        )

        )

        self.connection.commit()


    def get_all_history(self):

        self.cursor.execute("""

        SELECT *

        FROM execution_history

        ORDER BY id

        """)

        return self.cursor.fetchall()



    def clear_history(self):

        self.cursor.execute("""

        DELETE FROM execution_history

        """)

        self.connection.commit()



    def close(self):

        self.connection.close()
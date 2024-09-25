import sqlite3
from random import randrange

class DBHandler():
    db_file = "sidequests.db"
    _conn : sqlite3.Connection = None

    def _create_connection(self) -> None:
        self._conn = sqlite3.connect(self.db_file)
    
    def _close_connection(self) -> None:
        self._conn.close()
        self._conn = None

    def create_table(self, table_name : str, fields : str) -> None:
        try: 
            self._conn.execute("""
            CREATE TABLE {table_name} (
                {fields}
            )
            """.format(table_name=table_name,fields=fields))
        except sqlite3.OperationalError:
            print("Table already exists, skipping...\n")


class QuestsDBHandler(DBHandler):
    def create_quest_table(self):
        if (self._conn == None):
            self._create_connection()

        self.create_table("quests", 
            """id char[20],
            name char[20],
            daily bool,
            monthly bool,
            necessary bool,
            difficulty tinyint"""
        )

    def add_quest(self, quest_name : str, daily : bool = False, monthly : bool = False, necessary: bool = False, difficulty : int = 5):
        if (self._conn == None):
            self.create_connection()
        self._conn.execute("""
        INSERT INTO quests (id,name,daily,monthly,necessary,difficulty)
        VALUES ("{id}","{name}",'{daily}','{monthly}','{necessary}','{difficulty}');
        """.format(
            id = str(randrange(10 ** 9,10 ** 10)),
            name = quest_name,
            daily = daily,
            monthly = monthly,
            necessary = necessary,
            difficulty = difficulty
        ))
        self._close_connection()

    def get_quest(self, quest_id : str) -> list:
        if (self._conn == None):
            self.create_connection()
        n = self._conn.execute("""SELECT *
        FROM quests
        WHERE id = {quest_id} """.format(quest_id = quest_id)).fetchall()
        self._close_connection()
        return n

    def delete_quest(self, quest_id : str):
        if (self._conn == None):
            self.create_connection()
        self._conn.execute("DELETE FROM quests WHERE id = {quest_id}".format(quest_id = quest_id))
        self._close_connection()


quests = QuestsDBHandler()
quests.create_quest_table()
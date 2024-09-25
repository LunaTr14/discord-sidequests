import sqlite3
from random import randrange
def create_quest_table():
    conn = sqlite3.connect("quests.db")
    conn.execute("""CREATE TABLE quests (
        id char[20],
        name char[20],
        daily bool,
        monthly bool,
        necessary bool,
        difficulty tinyint
    ) """)
    conn.close()


def add_quest(quest_name : str, daily : bool = False, monthly : bool = False, necessary: bool = False, difficulty : int = 5):
    conn = sqlite3.connect("quests.db")
    conn.execute("""
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
    conn.commit()
    conn.close()

def get_quest(quest_id : str) -> list:
    conn = sqlite3.connect("quests.db")
    n = conn.execute("""SELECT *
    FROM quests
    WHERE id = {quest_id} """.format(quest_id = quest_id)).fetchall()
    conn.close()
    return n

def delete_quest(quest_id : str):
    conn = sqlite3.connect("quests.db")
    conn.execute("DELETE FROM quests WHERE id = {quest_id}".format(quest_id = quest_id))
    conn.commit()
    conn.close()
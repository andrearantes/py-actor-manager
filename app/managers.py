import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()


    def create(self, first_name, last_name) -> None:
        self.cursor.execute(f"INSERT INTO {self.table_name} (first_name, last_name)"
                            f" VALUES (?, ?)",
                            (first_name, last_name))
        self.connection.commit()


    def all(self) -> list[Actor]:
        self.cursor.execute(f"SELECT id, first_name,"
                            f" last_name FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [Actor(id=row[0], first_name=row[1],
                      last_name=row[2]) for row in rows]


    def update(self, pk, first_name, last_name) -> None:
        self.cursor.execute(f"UPDATE {self.table_name} SET first_name = ?,"
                            f" last_name = ? WHERE id = ?",
                            (first_name, last_name, pk))
        self.connection.commit()


    def delete(self, pk) -> None:
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?",
                            (pk,))
        self.connection.commit()

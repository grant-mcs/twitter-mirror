import os
import sqlite3
from sqlite3 import Connection
from sqlite3 import Cursor

class DB():
    connection: Connection
    cursor: Cursor

    @staticmethod
    def connect(dbPath=None):
        db = DB()
        dbPath = dbPath if dbPath else "data/twitter-mirror.db"
        needsInit = not os.path.exists(dbPath)
        db.connection = sqlite3.connect(dbPath)
        db.cursor = db.connection.cursor()

        if needsInit:
            with open("model/schema.sql", "r") as f:
                createScript = f.read()
                db.cursor.executescript(createScript)

        return db

    def execute(self, stmt: str, params: list=[]):
        self.cursor.execute(stmt, params)
        self.connection.commit()
        return self.cursor.rowcount

    def query(self, stmt: str, params: list=[]):
        self.cursor.execute(stmt, params)
        return self.cursor.fetchall()

    def query_value(self, stmt: str, params: list=[]):
        self.cursor.execute(stmt, params)
        tuple = self.cursor.fetchone()
        return tuple[0] if tuple else None

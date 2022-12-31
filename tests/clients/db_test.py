import os
import unittest

from clients.db import DB

class TestDB(unittest.TestCase):

    def setUp(self) -> None:
        # Ensure that the test DB is created each time
        if os.path.exists("data/test.db"):
            os.remove("data/test.db")

    def test_query(self):
        db = DB.connect("data/test.db")
        db.execute("CREATE TABLE test (col1 INT, col2 VARCHAR(32))")
        db.execute("INSERT INTO test (col1, col2) VALUES (123, 'ABCDEF')")
        db.execute("INSERT INTO test (col1, col2) VALUES (456, 'GHIJKL')")
        testRows = db.query("SELECT * FROM test")
        self.assertEqual(2, len(testRows))
        self.assertEqual("GHIJKL", testRows[1][1])

    def test_query_value(self):
        db = DB.connect("data/test.db")
        db.execute("CREATE TABLE test (col1 INT, col2 VARCHAR(32))")
        db.execute("INSERT INTO test (col1, col2) VALUES (123, 'ABCDEF')")
        db.execute("INSERT INTO test (col1, col2) VALUES (456, 'GHIJKL')")
        value = db.query_value("SELECT col2 FROM test WHERE col1 = 123")
        self.assertEqual("ABCDEF", value)

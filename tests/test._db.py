import unittest
from Auto-Entrepreneur.db import DB

class TestDB(unittest.TestCase):
    def test_db(self):
        db = DB("test_db")
        db["key"] = "value"
        self.assertEqual(db["key"], "value")
        del db["key"]
        with self.assertRaises(KeyError):
            db["key"]

if __name__ == "__main__":
    unittest.main()

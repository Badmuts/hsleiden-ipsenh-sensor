import unittest
from data.DatabaseScript import *
import os

class DatabaseScriptTest(unittest.TestCase):

    def setUp(self):
        self.dbPath = 'HUB_database.db'
        self.databaseScript = DatabaseScript(self.dbPath)

    def test_createDataTables(self):
        self.databaseScript.createDataTables()
        result = os.path.isfile(self.dbPath)

        self.assertTrue(result)

    def tearDown(self):
        dbExist = os.path.isfile(self.dbPath)
        if (dbExist):
            os.remove(self.dbPath)

if __name__ == '__main__':
    unittest.main()

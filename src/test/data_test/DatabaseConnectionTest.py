import unittest
from data.DatabaseConnection import *

class DatabaseConnectionTest(unittest.TestCase):

    def runTest(self):
        print 'hoi'

    def setUp(self):
        self.databaseConnection = DatabaseConnection()
        pass

    def test_hasApiKey(self):
        apiKey = self.databaseConnection.hasApiKeys()
        self.assertEqual(apiKey, False)


if __name__ == '__main__':
    DatabaseConnectionTest()

import unittest
from data.DatabaseConnection import *
import os

class DatabaseConnectionTest(unittest.TestCase):

    def runTest(self):
        pass

    def setUp(self):
        self.dbPath = 'HUB_database.db'
        self.databaseConnection = DatabaseConnection()

    def test_hasApiKey(self):
        apiKey = self.databaseConnection.hasApiKeys()
        self.assertFalse(apiKey)

    def test_registerHUB(self):
        self.databaseConnection.registerHUB("API_KEY")
        apiKey = self.databaseConnection.hasApiKeys()
        self.assertTrue(apiKey)

    def test_registerSensor(self):
        sensors = []

        sensors.append({
            "id": 1,
            "name": "in",
            "sensorType": "hc-sr04",
            "status": True,
            "gpio_trigger": 17,
            "gpio_echo": 18
        })

        sensors.append({
            "id": 2,
            "name": "out",
            "sensorType": "hc-sr04",
            "status": True,
            "gpio_trigger": 22,
            "gpio_echo": 23
        })

        self.databaseConnection.registerSensor(sensors)
        result = self.databaseConnection.getSensors()
        self.assertEqual(len(result), 2)


    def tearDown(self):
        dbExist = os.path.isfile(self.dbPath)
        if (dbExist):
            os.remove(self.dbPath)
            pass

if __name__ == '__main__':
    unittest.main()

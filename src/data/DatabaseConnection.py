import os.path
import sqlite3
from DatabaseScript import *
from datetime import datetime

class DatabaseConnection(object):

    def __init__(self):
        dbPath = 'HUB_database.db'

        dbExist = os.path.isfile(dbPath)
        if (not dbExist):
            createDb = DatabaseScript(dbPath)
            createDb.createDataTables()

        self.con = sqlite3.connect(dbPath)
        self.cur = self.con.cursor()

    def rawQuery(self, query):
        self.cur.execute(query)
        return self.cur.fetchone()

    def getApiKey(self):
        query = "SELECT * FROM api_connection"
        self.cur.execute(query)
        result = self.cur.fetchone()

        if result is None:
            return False

        return result

    def hasApiKeys(self):
        if not self.getApiKey():
            return False

        return True

    def registerHUB(self, api_key):
        self.cur.execute('INSERT INTO api_connection (api_key, datetime) VALUES (?, ?)', (api_key, str(datetime.now())))
        self.con.commit()

    def registerSensor(self, sensors):
        for sensor in sensors:
            self.cur.execute("INSERT INTO sensor (sensor_id, sensorType, name) VALUES (?, ?, ?)",
                             (sensor['id'], sensor['sensorType'], sensor['name']))
        self.con.commit()

    def getSensors(self):
        query = "SELECT sensor_id, sensorType, name FROM sensor"
        self.cur.execute(query)

        return self.cur.fetchall()

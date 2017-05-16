import os.path
import sqlite3
from DatabaseScript import *

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

    def checkApiRegister(self):
        query = "SELECT * FROM api_connection"
        self.cur.execute(query)

        if self.cur.fetchone() is None:
            return False

        return True

    def registerHUB(self, api_key):
        query = 'INSERT INTO api_connection (api_key) VALUES (' + api_key + ')'
        self.cur.execute(query)

    def registerSensor(self, type, id):
        query = 'INSERT INTO api_connection (api_key) VALUES (' + api_key + ')'
        self.cur.execute(query)
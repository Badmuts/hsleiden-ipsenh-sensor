import os.path
import sqlite3
from DatabaseScript import *

class DatabaseConnection(object):

    def __init__(self):
        dbPath = '../Data/HUB_database.db'

        dbExist = os.path.isfile(dbPath)
        if (not dbExist):
            createDb = DatabaseScript()
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
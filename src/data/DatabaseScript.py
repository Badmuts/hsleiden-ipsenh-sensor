import sqlite3

class DatabaseScript(object):

    def __init__(self, path):
        print'DatabaseScript'
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def createDataTables(self):
        query = []
        query.append('CREATE TABLE api_connection (id INTEGER PRIMARY KEY AUTOINCREMENT, api_key TEXT,datetime DATETIME);')
        query.append('CREATE TABLE sensor (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor_id INTEGER, sensorType TEXT, name TEXT);')

        for i in query:
            self.cur.execute(i)

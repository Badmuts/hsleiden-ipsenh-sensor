import sqlite3

class DatabaseScript(object):

    def __init__(self):
        print'DatabaseScript'
        self.con = sqlite3.connect("../Data/HUB_database.db")
        self.cur = self.con.cursor()

    def createDataTables(self):

        query = 'CREATE TABLE api_connection (id	INTEGER PRIMARY KEY AUTOINCREMENT, api_key TEXT,datetime DATETIME);'
        self.cur.execute(query)
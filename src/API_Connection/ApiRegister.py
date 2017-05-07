import requests
from Data.databaseConnection import *

class ApiRegister(object):

    def __init__(self, database):
        self.database = database
        print 'ApiRegister init'
        self.chechSensors()

    def chechSensors(self):
        resp = requests.get('https://api.github.com/users/jeroenvo1/repos')

        if resp.status_code != 200:
            print 'Call mislukt'

        print resp.json()

    def registerHub(self):
        resp = requests.get('https://api.github.com/users/jeroenvo1/repos')

        if resp.status_code != 200:
            print 'Call mislukt'

        print resp.json()
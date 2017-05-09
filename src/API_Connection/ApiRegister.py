import requests
from data.DatabaseConnection import *
from sensor.CheckSensor import *

class ApiRegister(object):

    def __init__(self, database):
        print 'ApiRegister init'

        self.chechSensors = CheckSensor()

    def getSensors(self):
        # call voor de ports
        resp = requests.get('https://api.github.com/users/jeroenvo1/repos')

        if resp.status_code != 200:
            print 'Call mislukt'

        # print resp.json()

        a = [17, 23]
        result = []
        for i in a:
            result.append(self.chechSensors.check(i))

        print result
        # return result

    def registerHub(self, sensors):
        resp = requests.post('https://api.github.com/users/jeroenvo1/repos', json=sensors.json())

        if resp.status_code != 200:
            print 'Call mislukt'

        return resp.json()
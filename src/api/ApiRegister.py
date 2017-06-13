import requests
import json
from hub.HubInformation import *
from config.Config import *
import threading

class ApiRegister(object):
    sensorData = []

    def __init__(self):
        self.config = Config()
        self.url = self.config.get('url')

        self.hubInformation = HubInformation()

    def registerHub(self, data):
        serial = self.hubInformation.getserial()

        resp = requests.post(self.url + '/hubs', json.dumps(data))

        if resp.status_code != 201:
            print 'Call mislukt'

        return resp.json()

    def sendData(self, data):
        self.sensorData.append(data)
        print "api len sensorData:", len(self.sensorData)
        if len(self.sensorData) == 2:
            t1 = threading.Thread(target=self.dataApiCall())
            t1.start()
            self.sensorData = []

    def dataApiCall(self):
        print "data:"
        print json.dumps(self.sensorData)

        resp = requests.post(self.url + '/datapoints', json.dumps(self.sensorData))

        if resp.status_code != 201:
            print 'Call mislukt'
        else:
            print "sendData gelukt"
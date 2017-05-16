import requests
import json
from hub.HubInformation import *


class ApiRegister(object):

    def __init__(self, database):
        print 'ApiRegister init'
        self.hubInformation = HubInformation()

    def registerHub(self, data):
        serial = self.hubInformation.getserial()

        resp = requests.post('http://192.168.1.239:8080/gpiorevision', json=data)

        if resp.status_code != 200:
            print 'Call mislukt'

        return resp.json()
import requests
import json
from hub.HubInformation import *
from config.config import *

class ApiRegister(object):

    def __init__(self, database):
        print 'ApiRegister init'
        self.config = Config()
        self.url = self.config.get('url')

        self.hubInformation = HubInformation()

    def registerHub(self, data):
        serial = self.hubInformation.getserial()

        resp = requests.post(self.url + 'healthz', json=serial)

        if resp.status_code != 200:
            print 'Call mislukt'

        return resp.json()
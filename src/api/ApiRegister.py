import requests
import json
from hub.HubInformation import *
from config.Config import *

class ApiRegister(object):

    def __init__(self, database):
        self.config = Config()
        self.url = self.config.get('url')

        self.hubInformation = HubInformation()

    def registerHub(self, data):
        serial = self.hubInformation.getserial()

        resp = requests.post(self.url + 'hubs', json.dumps(data))

        if resp.status_code != 201:
            print 'Call mislukt'

        return resp.json()

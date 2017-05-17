from data.DatabaseConnection import *
from api.ApiRegister import *
from sensor.OccupationSensor import *
from config.Config import *
from hub.HubInformation import *
import json

class main(object):

    def __init__(self):
        self.setConfig()

        hubInformation = HubInformation()
        database = DatabaseConnection()
        registered = database.hasApiKeys()

        if (not registered):
            sensors = []
            sensors.append(OccupationSensor('in', 'hc-sr04', 17))
            sensors.append(OccupationSensor('out', 'hc-sr04', 23))

            dataSensors = []
            for i in sensors:
                dataSensors.append({
                    "name": i.getName(),
                    "sensorType": i.getType(),
                    "status": i.getStatus()
                })

            data = {
                "serialNumber": hubInformation.getserial(),
                "name": "Raspberry Pi",
                "sensors": dataSensors

            }

            api = ApiRegister(database)
            register = api.registerHub(data)
            database.registerHUB(register['id'])
            database.registerSensor(register['sensors'])

    def setConfig(self):
        f = open("../config.json")
        conf = json.loads(f.read())
        f.close()

        configObject = Config()
        configObject.setConfig(conf)

if __name__ == '__main__':
    main()

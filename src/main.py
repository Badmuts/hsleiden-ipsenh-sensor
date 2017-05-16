from data.DatabaseConnection import *
from api.ApiRegister import *
from sensor.OccupationSensor import *
from config.config import *

class main(object):

    def __init__(self):
        self.setConfig()

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
                    "type": i.getType(),
                    "status": i.getStatus()
                })

            data = {
                "serialNumber": "0000000000000000",
                "sensors": [
                    dataSensors
                ]
            }

            api = ApiRegister(database)
            register = api.registerHub(data)
            database.registerHUB("API KEY")
            database.registerSensor()

    def setConfig(self):
        f = open("../../config.json")
        conf = json.loads(f.read())
        f.close()

        configObject = Config()
        configObject.setConfig(conf)

if __name__ == '__main__':
    main()

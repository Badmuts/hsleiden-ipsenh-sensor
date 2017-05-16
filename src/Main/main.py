from data.DatabaseConnection import *
from api.ApiRegister import *
from sensor.OccupationSensor import *

class main(object):

    def __init__(self):
        database = DatabaseConnection()
        registered = database.checkApiRegister()

        if (not registered):
            sensors = []
            sensors.append(OccupationSensor('sensor 1', 'hc-sr04', 17))
            sensors.append(OccupationSensor('sensor 2', 'hc-sr04', 23))

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
            database.registerHUB()
            database.registerSensor()




if __name__ == '__main__':
    main()

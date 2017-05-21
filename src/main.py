from data.DatabaseConnection import *
from api.Api import *
from sensor.OccupationSensor import *
from config.Config import *
from hub.HubInformation import *
import json
from sensor.OccupationSensorScript import *
import threading

class main(object):

    def __init__(self):
        self.setConfig()

        self.database = DatabaseConnection()
        hubInformation = HubInformation()
        hasApiKey = self.database.hasApiKeys()

        sensors = []

        if (not hasApiKey):
            sensors.append(OccupationSensor('in', 'hc-sr04', 18, 17, None))
            sensors.append(OccupationSensor('out', 'hc-sr04', 24, 23, None))

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

            api = Api()
            register = api.registerHub(data)
            self.database.registerHUB(register['id'])
            self.database.registerSensor(register['sensors'])

        s = OccupationSensorScript(OccupationSensor('in', 'hc-sr04', 18, 17, '591ca76746b69a5cb52f9d9b'))
        s.sensor_thread()
        # t = threading.Thread(target=s.sensor_thread())

        # sensors = self.getSensors()
        # print 'begin thread loop'
        # for sensor in sensors:
        #     print 'thread loop'
        #     if sensor.getStatus():
        #         print 'True if thread loop'
        #         s = OccupationSensorScript(sensor)
        #         t = threading.Thread(target = s.sensor_thread())
        #         t.start()

    def getSensors(self):
        data = self.database.getSensors()
        sensors = []

        for i in data:
            if i[2] == "in":
                sensors.append(OccupationSensor('in', 'hc-sr04', 18, 17, i[0]))
            else:
                sensors.append(OccupationSensor('out', 'hc-sr04', 24, 23, i[0]))
        return sensors

    def setConfig(self):
        f = open("../config.json")
        conf = json.loads(f.read())
        f.close()

        configObject = Config()
        configObject.setConfig(conf)

if __name__ == '__main__':
    main()

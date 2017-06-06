from data.DatabaseConnection import *
from api.ApiRegister import *
from sensor.OccupationSensor import *
from config.Config import *
from hub.HubInformation import *
import json
from sensor.OccupationSensorScript import *
from sensor.OccupationSensorScriptTest import *

class main(object):

    def __init__(self):
        self.setConfig()

        hubInformation = HubInformation()
        api = ApiRegister()
        database = DatabaseConnection()
        registered = database.hasApiKeys()

        if (not registered):
            data = {
                "serialNumber": hubInformation.getserial(),
                "name": "Raspberry Pi",
                "sensors": self.createSensors()
            }


            register = api.registerHub(data)
            database.registerHUB(register['id'])
            database.registerSensor(register['sensors'])
            sensors = self.getSensors(database)

        else:
            sensors = self.getSensors(database)

        threads = []
        for i in sensors:
            threads.append(OccupationSensorScript(i.getGpioTrigger(), i.getGpioEcho(), i.getSensorId(), i.getName(), api))
            threads[len(threads)-1].start()

        print "main klaar"

        # self.sensorAlive(threads)

    def getSensors(self, database):
        sensors = []
        s = database.getSensors()

        for i in s:
            sensors.append(OccupationSensor(i[1], i[3], i[2], i[4], i[5]))

        return sensors

    def createSensors(self):
        sensors = []

        sensors.append({
            "name": "in",
            "sensorType": "hc-sr04",
            "status": True,
            "gpio_trigger": 17,
            "gpio_echo": 18
        })

        sensors.append({
            "name": "out",
            "sensorType": "hc-sr04",
            "status": True,
            "gpio_trigger": 22,
            "gpio_echo": 23
        })
        return sensors

    def sensorAlive(self, threads):
        while True:
            time.sleep(2)
            for t in threads:
                if not t.isAlive():
                    print "starting new thread"
                    t.start()


    def setConfig(self):
        f = open("../config.json")
        conf = json.loads(f.read())
        f.close()

        configObject = Config()
        configObject.setConfig(conf)

if __name__ == '__main__':
    main()

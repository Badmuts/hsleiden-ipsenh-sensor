from sensor.CheckSensor import *

class Sensor(object):

    def __init__(self, name, type, gpioTrigger, gpioEcho, sensorId):
        self.name = name
        self.type = type
        self.gpioTrigger = gpioTrigger
        self.gpioEcho = gpioEcho
        self.sensorId = sensorId

        self.checkSensor = CheckSensor()
        self.status = self.checkSensor.isSensorAvailable(self.gpioEcho)
        # self.status = True

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getStatus(self):
        return self.status

    def setSensorId(self, sensorId):
        self.sensorId = sensorId

    def getGpioEcho(self):
        return self.gpioEcho

    def getGpioTrigger(self):
        return self.gpioTrigger

    def getSensorId(self):
        return self.sensorId

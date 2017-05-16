from sensor.CheckSensor import *

class Sensor(object):

    def __init__(self, name, type, gpioTrigger, gpioEcho):
        self.name = name
        self.type = type
        self.gpioTrigger = gpioTrigger
        self.gpioEcho = gpioEcho

        self.checkSensor = CheckSensor()
        self.status = self.checkSensor.isSensorAvailable(self.gpioTrigger)

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getGpioTrigger(self):
        return self.gpioTrigger

    def getGpioEcho(self):
        return self.gpioEcho

    def getStatus(self):
        return self.status

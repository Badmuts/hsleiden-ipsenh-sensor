from sensor.CheckSensor import *

class Sensor(object):

    def __init__(self, name, type, gpioTrigger):
        self.name = name
        self.type = type
        self.gpioTrigger = gpioTrigger

        self.checkSensor = CheckSensor()
        self.status = self.checkSensor.check(self.gpioTrigger)

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getGpioTrigger(self):
        return self.gpioTrigger

    def getStatus(self):
        return self.status

from sensor.CheckSensor import *

class Sensor(object):

    def __init__(self, name, type, gpioEcho):
        self.name = name
        self.type = type
        self.gpioEcho = gpioEcho

        self.checkSensor = CheckSensor()
        self.status = self.checkSensor.isSensorAvailable(self.gpioEcho)

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getGpioEcho(self):
        return self.gpioEcho

    def getStatus(self):
        return self.status

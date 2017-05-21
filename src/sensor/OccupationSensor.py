from sensor.Sensor import *

class OccupationSensor(Sensor):

    def __init__(self, name, type, gpioTrigger, gpioEcho, sensorId):
        super(OccupationSensor, self).__init__(name, type, gpioTrigger, gpioEcho, sensorId)

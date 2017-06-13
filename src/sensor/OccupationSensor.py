from sensor.Sensor import *

class OccupationSensor(Sensor):


    def __init__(self, sensorId, name, type, gpioTrigger, gpioEcho):
        super(OccupationSensor, self).__init__(sensorId, name, type, gpioTrigger, gpioEcho)
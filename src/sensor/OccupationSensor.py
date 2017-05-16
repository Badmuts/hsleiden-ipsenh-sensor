from sensor.Sensor import *

class OccupationSensor(Sensor):

    def __init__(self, name, type, gpioTrigger):
        super(OccupationSensor, self).__init__(name, type, gpioTrigger)

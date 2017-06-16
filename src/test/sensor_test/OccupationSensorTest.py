import unittest
from sensor.OccupationSensor import *

class OccupationSensorTest(unittest.TestCase):

    def setUp(self):
        self.occupationSensor = OccupationSensor(1, 'in', 'hc-sr04', 17, 18)

    def test_getSensorId(self):
        sensorId = self.occupationSensor.getSensorId()
        self.assertEqual(sensorId, 1)

    def test_getName(self):
        sensorName = self.occupationSensor.getName()
        self.assertEqual(sensorName, 'in')

    def test_getType(self):
        sensorType = self.occupationSensor.getType()
        self.assertEqual(sensorType, 'hc-sr04')

    def test_getGpioTrigger(self):
        sensorGpioTrigger = self.occupationSensor.getGpioTrigger()
        self.assertEqual(sensorGpioTrigger, 17)

    def test_getGpioEcho(self):
        sensorGpioEcho = self.occupationSensor.getGpioEcho()
        self.assertEqual(sensorGpioEcho, 18)

if __name__ == '__main__':
    unittest.main()

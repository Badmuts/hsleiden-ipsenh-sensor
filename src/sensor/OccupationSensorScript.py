import RPi.GPIO as GPIO
import time
from api.Api import *
import threading

class OccupationSensorScript(object):
    def __init__(self, sensor):
        self.api = Api()

        self.gpioTrigger = sensor.getGpioTrigger()
        self.gpioEcho = sensor.getGpioEcho()
        self.sensorId = sensor.getSensorId()

    def setupPins(self):
        GPIO.setmode(GPIO.BCM)

    def refreshPins(self):
        GPIO.setup(self.gpioTrigger, GPIO.OUT)
        GPIO.setup(self.gpioEcho, GPIO.IN)

        GPIO.output(self.gpioTrigger, False)

        GPIO.output(self.gpioTrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.gpioTrigger, False)

    def sensor_thread(self):
        print "run sensor_thread"
        GPIO.setwarnings(False)
        data = []

        startTime = time.time()
        for i in range(1000):
            self.setupPins()
            self.refreshPins()

            while GPIO.input(self.gpioEcho) == 0:
                pulse_start = time.time()

            while GPIO.input(self.gpioEcho) == 1:
                pulse_end = time.time()

            try:
                pulse_duration = pulse_end - pulse_start
            except UnboundLocalError:
                pulse_start = time.time()
                pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            distance = round(distance, 2)

            data.append({
                "key": "distance",
                "value": distance,
                "timestamp": int(pulse_start)
            })

            GPIO.cleanup()

            time.sleep(0.08)
            endTime = time.time()
            # print 'endTime: ', endTime
            # print 'startTime: ', startTime
            # print endTime - startTime

            if endTime - startTime >= 10:
                startTime = time.time()
                self.sendData(data)
                data = []

    def sendData(self, data):
        data = {
            "sensor_id": self.sensorId,
            "data": data
        }

        t1 = threading.Thread(target = self.api.sendData(data))
        t1.start()

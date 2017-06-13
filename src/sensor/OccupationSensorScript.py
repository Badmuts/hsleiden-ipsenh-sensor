import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
class OccupationSensorScript(threading.Thread):
    def __init__(self, gpioTrigger, gpioEcho, sensorId, name, api):
        threading.Thread.__init__(self)
        self.api = api

        self.gpioTrigger = gpioTrigger
        self.gpioEcho = gpioEcho
        self.sensorId = sensorId
        self.name = name

    def run(self):
        print "run sensor_thread. Trigger:", self.gpioTrigger
        # GPIO.setwarnings(False)
        data = []

        startTime = time.time()
        while True:
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

            if endTime - startTime >= 5:
                print "if in trigger:", self.gpioTrigger
                self.sendData(data)
                startTime = time.time()
                data = []

    def setupPins(self):
        GPIO.setmode(GPIO.BCM)

    def refreshPins(self):
        GPIO.setup(self.gpioTrigger, GPIO.OUT)
        GPIO.setup(self.gpioEcho, GPIO.IN)

        GPIO.output(self.gpioTrigger, False)

        GPIO.output(self.gpioTrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.gpioTrigger, False)

    def sendData(self, data):
        data = {
            "sensor_id": self.sensorId,
            "name": self.name,
            "data": data
        }

        self.api.sendData(data)

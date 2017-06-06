import time
from api.ApiRegister import *
import threading

class OccupationSensorScriptTest(threading.Thread):
    def __init__(self, gpioTrigger, gpioEcho, sensorId):
        threading.Thread.__init__(self)
        self.api = ApiRegister()

        self.gpioTrigger = gpioTrigger
        self.gpioEcho = gpioEcho
        self.sensorId = sensorId

    def run(self):
        print "run sensor_thread"
        print "gpioTrigger", self.gpioTrigger
        data = []

        startTime = time.time()
        for i in range(1000000):

            pulse_start = time.time()
            time.sleep(0.02)

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


            time.sleep(0.08)
            endTime = time.time()
            # print 'endTime: ', endTime
            # print 'startTime: ', startTime
            # print endTime - startTime

            if endTime - startTime >= 5:
                print "if in trigger:", self.gpioTrigger
                self.sendData(data)
                startTime = time.time()
                # data = []


    def sendData(self, data):
        data = [{
            "sensor_id": self.sensorId,
            "data": data
        }]

        self.api.sendData(data)

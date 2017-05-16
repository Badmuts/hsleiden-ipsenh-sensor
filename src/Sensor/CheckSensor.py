from time import sleep
import RPi.GPIO as GPIO

class CheckSensor(object):

    def __init__(self):
        print 'CheckSensor init'

    def check(self, pin):
        GPIO.setmode(GPIO.BCM)

        # Set our input pin to be an input
        GPIO.setup(pin, GPIO.IN)

        value = None
        # Start a loop that never ends
        for i in range(0, 10):
            # Physically read the pin now
            if (GPIO.input(pin) == True):
                value = True
                break
            else:
                value = False

            sleep(1)

        return value
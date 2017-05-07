import time
import RPi.GPIO as GPIO
import threading

class CheckSensor(object):

    def __init__(self):
        self.GPIO_TRIGGER_TEST = False
        self.GPIO_ECHO_TEST = False
        self.test(17, 18)

    def test(self, trigger, echo):

        # instead of physical pin numbers
		GPIO.setmode(GPIO.BCM)

        # Define GPIO to use on Pi
		# 23 17
		GPIO_TRIGGER = trigger
        # 24 18
        GPIO_ECHO    = echo

        print "Ultrasonic Measurement"

        # Set pins as output and input
		# Trigger
		GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
        # Echo
        GPIO.setup(GPIO_ECHO,GPIO.IN)

        # Set trigger to False (Low)
        GPIO.output(GPIO_TRIGGER, False)

        # Allow module to settle
        time.sleep(0.5)

        # Send 10us pulse to trigger
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        start = time.time()

        t1 = threading.Thread(target = sensorTimer)
        t1.start()

        while GPIO.input(GPIO_ECHO)==0:
            start = time.time()

        while GPIO.input(GPIO_ECHO)==1:
            stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34300

        # That was the distance there and back so halve the value
        distance = distance / 2

        print "Distance : %.1f" % distance + ' cm'

        # Reset GPIO settings
        GPIO.cleanup()

        if(self.GPIO_TRIGGER_TEST and self.GPIO_ECHO_TEST):
            print 'Aangesloten'

        def sensorTimer(self, seconds):
            for i in range (0, 10):
                time.sleep(1)
                print 'sleep: ' + i

if __name__ == '__main__':
    CheckSensor()
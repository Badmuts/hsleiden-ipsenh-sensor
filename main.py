import RPi.GPIO as GPIO
import time
from datetime import datetime
import threading


def sensor_thread():
    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24

    print "Distance Measurement In Progress"

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while True:
        # print GPIO.input(ECHO)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        # if distance < 100:
        # 	print "Persoon!"
        # 	print "Afstand:", distance, "cm"
        # 	print "Tijd:", datetime.now().strftime('%Y-%m-%d %H:%M:%S') , "\n"
        # time.sleep(0.5)

        print "Distance:", distance, "cm"

        GPIO.cleanup()

        time.sleep(1)
        # time.sleep(0.1)

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)


t1 = threading.Thread(target=sensor_thread)
t1.start()

while True:
    time.sleep(2)

    if not t1.isAlive():
        print "Thread chrashed"
        print "Thread starting...."
        print " "

        t1 = threading.Thread(target=sensor_thread)
        t1.start()




# #!/usr/bin/python
# #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# #|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
# #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# #
# # ultrasonic_1.py
# # Measure distance using an ultrasonic module
# #
# # Author : Matt Hawkins
# # Date   : 09/01/2013

# # Import required Python libraries
# import time
# import RPi.GPIO as GPIO

# # Use BCM GPIO references
# # instead of physical pin numbers
# GPIO.setmode(GPIO.BCM)

# # Define GPIO to use on Pi
# GPIO_TRIGGER = 23
# GPIO_ECHO    = 24

# print "Ultrasonic Measurement"

# # Set pins as output and input
# GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
# GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# # Set trigger to False (Low)
# GPIO.output(GPIO_TRIGGER, False)

# # Allow module to settle
# time.sleep(0.5)

# # Send 10us pulse to trigger
# GPIO.output(GPIO_TRIGGER, True)
# time.sleep(0.00001)
# GPIO.output(GPIO_TRIGGER, False)
# start = time.time()

# while GPIO.input(GPIO_ECHO)==0:
#   start = time.time()

# while GPIO.input(GPIO_ECHO)==1:
#   stop = time.time()

# # Calculate pulse length
# elapsed = stop-start

# # Distance pulse travelled in that time is time
# # multiplied by the speed of sound (cm/s)
# distance = elapsed * 34300

# # That was the distance there and back so halve the value
# distance = distance / 2

# print "Distance : %.1f" % distance

# # Reset GPIO settings
# GPIO.cleanup()

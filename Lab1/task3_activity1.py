import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED
led = 23

# Set GPIO23 as output.
GPIO.setup(led, GPIO.OUT)

"""
TO DO 3.1
this function turns on the LED at led 
waits for duration t
turns off the LED
waits for duration t
"""

def blink( t,led=23 ):
    GPIO.output(led, GPIO.HIGH)  # turn on the LED
    sleep(t)
    GPIO.output(led, GPIO.LOW)  # turn off the LED


    
frequency = float(input("enter the frequency of blinks in cycles per second"))

while True:
    blink(60/frequency,led)




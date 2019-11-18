#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 31
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
               print("Motion Detected")

print("PIR module test")
sleep(2)
print("Ready")

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              sleep(100)
except KeyboardInterrupt:
               print("Quit")
               GPIO.cleanup()

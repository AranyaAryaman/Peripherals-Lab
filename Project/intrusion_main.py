#!/usr/bin/python
import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 38
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
press = 0

def MOTION(PIR_PIN):
    print("Motion Detected")
    if (press==1):
        print("Intruder!")

print("PIR module test")
sleep(2)
print("Ready")
GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
sleep(2)

while True:
    if ( GPIO.input(26) == False ):
        if (press==0):
            press = 1
            print("Alert System Activated")
        else:
            press = 0
            print("Alert System Deactivated")
        print("Button Pressed")
        os.system('date') # print the systems date and time
        print(GPIO.input(26))
        sleep(5)
    else:
        #os.system('clear') # clear the screens text
        #print ("Waiting for you to press a button")
        sleep(0.1)

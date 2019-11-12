#!/usr/bin/python

import os
from time import sleep
import RPi.GPIO as GPIO

BUZZ_PIN = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ_PIN,GPIO.OUT)

loop_count = 0

# define a function called morsecode
def morsecode ():
    #Dot Dot Dot
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.1)

    #Dash Dash Dash
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.2)
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.2)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.2)
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.2)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.2)
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.2)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.2)

    #Dot Dot Dot
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.HIGH)
    sleep(.1)
    GPIO.output(BUZZ_PIN,GPIO.LOW)
    sleep(.7)

#os.system('clear')
print("Morse Code")
morsecode()

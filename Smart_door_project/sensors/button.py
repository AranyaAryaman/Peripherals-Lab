
#!/usr/bin/python

import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
BUTTON_PIN = 40
# setup our input pin
# we use an internal pull up resistor to hold the pin at 3v3, otherwise the inputs value could chatter between high and low

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if ( GPIO.input(BUTTON_PIN) == False ):
        print("Button Pressed")
        os.system('date') # print the systems date and time
        print(GPIO.input(BUTTON_PIN))
        sleep(5)
    else:
        os.system('clear') # clear the screens text
        print ("Waiting for you to press a button")
        sleep(0.1)

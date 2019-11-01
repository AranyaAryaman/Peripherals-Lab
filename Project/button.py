
#!/usr/bin/python

import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# setup our input pin
# we use an internal pull up resistor to hold the pin at 3v3, otherwise the inputs value could chatter between high and low

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if ( GPIO.input(26) == False ):
        print("Button Pressed")
        os.system('date') # print the systems date and time
        print(GPIO.input(26))
        sleep(5)
    else:
        os.system('clear') # clear the screens text
        print ("Waiting for you to press a button")
        sleep(0.1)

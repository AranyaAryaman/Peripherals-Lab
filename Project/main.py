#!/usr/bin/env python

# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical la$

# Set up pin 11 for PWM
GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin
p.start(0)

reader = SimpleMFRC522()

try:
	id, text = reader.read()
	if id==853453118124:
		print("Access Granted")
		# Move the servo back and forth
		p.ChangeDutyCycle(3)     # Changes the pulse width to 3 (so moves the servo)
		sleep(1)                 # Wait 1 second
		p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
		sleep(1)
		# Clean up everything
		p.stop()                 # At the end of the program, stop the PWM
	else:
		print("Access Denied")
	print(id)
	print(text)
finally:
	GPIO.cleanup()

#!/usr/bin/env python

# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

from mfrc522 import SimpleMFRC522
import settings

GPIO.setmode(GPIO.BOARD) # Sets the pin numbering syste$
GPIO.setwarnings(False)

reader = SimpleMFRC522()

def run():
	print("Access Granted")
	settings.pir_on = False
	# Move the servo back and forth
	# Set up pin 11 for PWM
	GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
	p = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin

	p.start(0)
	p.ChangeDutyCycle(7)     # Changes the pulse width to 7 (so moves the servo)
	sleep(10)                 # Wait 10 seconds
	i=8
	while i<=12:
		#if (settings.pir_detect==True and settings.pir_on==True):
		#    p.ChangeDutyCycle(7)
		#    i=8
		p.ChangeDutyCycle(i)    # Changes the pulse width to 12 (so mov$
		i+=1
		sleep(1)

	p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
	sleep(1)
	# Clean up everything
	p.stop()                 # At the end of the program, stop the PWM


while(True):
	try:
		id, text = reader.read()
		if id==853453118124:
			run()
		else:
			print("Access Denied")
		print(id)
		print(text)
	finally:
		pass

GPIO.cleanup()


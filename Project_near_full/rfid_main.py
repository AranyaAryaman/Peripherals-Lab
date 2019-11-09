#!/usr/bin/env python

# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

from mfrc522 import SimpleMFRC522
import settings

LED_PIN = 40
SERVO_PIN = 12
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering syste$
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)

reader = SimpleMFRC522()

def run():
	print("Access Granted")
	settings.pir_on = False
	# Move the servo back and forth
	# Set up pin 11 for PWM
	GPIO.setup(SERVO_PIN,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
	p = GPIO.PWM(SERVO_PIN, 50)     # Sets up pin 11 as a PWM pin

	p.start(0)
	p.ChangeDutyCycle(7)     # Changes the pulse width to 7 (so moves the servo)
	sleep(8)                 # Wait 10 seconds
	i = 6
	while i<8:
		print("LED on")
		GPIO.output(LED_PIN,GPIO.HIGH)
		sleep(1)
		print("LED off")
		GPIO.output(LED_PIN,GPIO.LOW)
		i+=1
	while i<=12:
		if (settings.pir_detect==True):
			p.ChangeDutyCycle(7)
			i=8
			sleep(1)
		p.ChangeDutyCycle(i)    # Changes the pulse width to 12 (so mov$
		i+=1
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


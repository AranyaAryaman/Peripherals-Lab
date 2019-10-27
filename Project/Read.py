#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	id, text = reader.read()
	if id==853453118124:
		print("Access Granted")
	else:
		print("Access Denied")
	print(id)
	print(text)
finally:
	GPIO.cleanup()

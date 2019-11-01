#!/usr/bin/python
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# setup our input pin
# we use an internal pull up resistor to hold the pin at 3v3, otherwise the inp$
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
MQTT_PATH = "door"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
client = mqtt.Client()

while True:
    if ( GPIO.input(40) == False ):
        print("Button Pressed")
        publish.single("door", "Let me enter", hostname="10.42.0.1")
        os.system('date') # print the systems date and time
        print(GPIO.input(40))
        sleep(5)
    else:
        os.system('clear') # clear the screens text
        print ("Waiting for you to press a button")
        sleep(0.1)
 

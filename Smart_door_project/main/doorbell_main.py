#!/usr/bin/python
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import os
from time import sleep
import RPi.GPIO as GPIO
from pad4pi import rpi_gpio

#******************************************#
KEYPAD = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

COL_PINS = [17, 4, 3, 2] # BOARD numbering
ROW_PINS = [12,5,22,27] # BOARD numbering

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#******************************************#

MSG = ""
BUTTON_PIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup our input pin
# we use an internal pull up resistor to hold the pin at 3v3, otherwise the inp$
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global pm
global system_sts

def printKey(key):
  global MSG
  key=ord(key)
  if key==0x30:
    MSG += "0"
  if key==0x31:
    MSG += "1"
  if key==0x32:
    MSG += "2"
  if key==0x33:
    MSG += "3"
  if key==0x34:
    MSG += "4"
  if key==0x35:
    MSG += "5"
  if key==0x36:
    MSG += "6"
  if key==0x37:
    MSG += "7"
  if key==0x38:
    MSG += "8"
  if key==0x39:
    MSG += "9"
  if key==0x41:
    MSG += "A"
  if key==0x42:
    MSG += "B"
  if key==0x43:
    MSG += "C"
  if key==0x44:
    MSG += "D"
  if key==0x23:
    MSG += "#"
  if key==0x2a:
    MSG += "*"

#******************************************#
# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

 
MQTT_PATH = "door"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
client = mqtt.Client()

while True:
    if ( GPIO.input(BUTTON_PIN) == False ):
        print("Button Pressed")
        print("Message is ", MSG)
        publish.single("door", MSG, hostname="broker.hivemq.com")
        MSG = ""
        os.system('date') # print the systems date and time
        print(GPIO.input(BUTTON_PIN))
        sleep(5)
    else:
        sleep(0.1)
 

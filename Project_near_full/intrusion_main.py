#!/usr/bin/python
import os
import RPi.GPIO as GPIO
from time import sleep
import settings
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

settings.init()
GPIO.setmode(GPIO.BOARD)
BUZZ_PIN = 33
PIR_PIN = 31
BUTTON_PIN = 36
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZ_PIN,GPIO.OUT)

# define a function called morsecode - SOS msg
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

def MOTION(PIR_PIN):
    print("Motion Detected")
    settings.pir_detect=True
    if (settings.pir_on==True):
        print("Intruder Alert!")
        publish.single("door", "Intruder Alert", hostname="broker.hivemq.com")
        morsecode()
    else:
        print("Motion Ignored (Deactivated)!")
    sleep(5)
    settings.pir_detect=False

MQTT_PATH = "door"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
client = mqtt.Client()

print("PIR module test")
sleep(2)
print("Ready")
GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
sleep(2)

while True:
    if ( GPIO.input(BUTTON_PIN) == False ):
        if (settings.pir_on==False):
            settings.pir_on = True
            print("Alert System Activated")
        else:
            settings.pir_on = False
            print("Alert System Deactivated")
        print("Button Pressed")
        os.system('date') # print the systems date and time
        sleep(1)
    else:
        #os.system('clear') # clear the screens text
        #print ("Waiting for you to press a button")
        sleep(0.1)

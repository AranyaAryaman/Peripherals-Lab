import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
import settings
from goto import with_goto

MQTT_SERVER = "broker.hivemq.com"
MQTT_PATH = "main_door"

LED_PIN = 10
SERVO_PIN = 12
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical la$
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)

@with_goto
def run(msg):
    try:
        if msg=="pass":
            print("Access Granted")
            f = open("demo.txt", "w")
            f.write("deactivate")
            f.close()
            # Move the servo back and forth
            GPIO.setup(SERVO_PIN,GPIO.OUT)  # Sets up pin SERVO_PIN to an output (instead of an input)
            p = GPIO.PWM(SERVO_PIN, 50)     # Sets up pin SERVO_PIN as a PWM pin

            p.start(0)

            label .starter
            p.ChangeDutyCycle(7)     # Changes the pulse width to 7 (so moves the servo)
            sleep(10)                 # Wait 10 second
            i = 6
            while i<8:
                    #print("LED on")
                    GPIO.output(LED_PIN,GPIO.HIGH)
                    sleep(1)
                    #print("LED off")
                    GPIO.output(LED_PIN,GPIO.LOW)
                    i+=1

            while i<=12:
                p.ChangeDutyCycle(i)    # Changes the pulse width to 12 (so moves the servo)
                i+=1
                sleep(1)
        # Clean up everything
            p.stop()                 # At the end of the program, stop the PWM
            f = open("demo.txt", "w")
            f.write("activated")
            f.close()
        else:
            print("Access Denied")
    finally:
        pass

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, msg, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    passwd = msg.payload.decode("utf-8")
    if(passwd=="quit"):
        GPIO.cleanup()
    run(passwd)
    # more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program

MQTT_SERVER = "10.42.0.120"
MQTT_PATH = "test_channel"

GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical la$
GPIO.setwarnings(False)

def run(msg):
	try:
		if msg=="pass":
			print("Access Granted")
		# Move the servo back and forth
			# Set up pin 11 for PWM
			GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
			p = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin

			p.start(0)
			p.ChangeDutyCycle(7)     # Changes the pulse width to 7 (so moves the servo)
			sleep(10)                 # Wait 10 second
			p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
			sleep(1)
		# Clean up everything
			p.stop()                 # At the end of the program, stop the PWM
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

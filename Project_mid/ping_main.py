import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 35
ECHO = 37
print("Distance Measurement In Progress")

def run():
	print("Opening...")
	# Move the servo back and forth
	# Set up pin 11 for PWM
	GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
	p = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin

	p.start(0)
	p.ChangeDutyCycle(7)     # Changes the pulse width to 7 (so moves the servo)
	sleep(10)                 # Wait 10 seconds
	p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
	sleep(1)
	# Clean up everything
	p.stop()                 # At the end of the program, stop the PWM
	print("Closing...")

while(True):
	sleep(2)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)
	print("Waiting For Sensor To Settle")
	sleep(2)
	GPIO.output(TRIG, True)
	sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration*17150
	distance = round(distance, 2)
	print("Distance: "+str(distance)+"cm")
	if(distance<=7):
		run()
GPIO.cleanup()




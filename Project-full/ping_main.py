import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_PIN = 40
SERVO_PIN = 12
TRIG = 35
ECHO = 37
print("Distance Measurement In Progress")

GPIO.setup(LED_PIN,GPIO.OUT)

def run():
	print("Opening...")
	# Move the servo back and forth
	# Set up pin 11 for PWM
	GPIO.setup(SERVO_PIN,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
	p = GPIO.PWM(SERVO_PIN, 50)     # Sets up pin 11 as a PWM pin

	p.start(0)
	p.ChangeDutyCycle(7)     # Changes the pulse width to 7 (so moves the servo)
	sleep(10)                 # Wait 10 seconds
	i = 6
	while i<8:
		print("LED on")
		GPIO.output(LED_PIN,GPIO.HIGH)
		sleep(1)
		print("LED off")
		GPIO.output(LED_PIN,GPIO.LOW)
		i+=1
	while i<=12:
		#if (settings.pir_detect==True and settings.pir_on==True):
		#    p.ChangeDutyCycle(7)
		#    i=8
		p.ChangeDutyCycle(i)    # Changes the pulse width to 12 (so mov$
		i+=1
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




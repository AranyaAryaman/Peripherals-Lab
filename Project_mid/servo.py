# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
GPIO.setup(12,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(12, 50)     # Sets up pin 11 as a PWM pin
p.start(0)               # Starts running PWM on the pin and sets it to 0

# Move the servo back and forth
p.ChangeDutyCycle(7)     # Changes the pulse width to 3 (so moves the servo)
sleep(1)
steps = [8,9,10,11,12]
for i in steps:
    p.ChangeDutyCycle(i)    # Changes the pulse width to 12 (so moves the servo)
    sleep(1)
# Clean up everything
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()           # Resets the GPIO pins back to defaults

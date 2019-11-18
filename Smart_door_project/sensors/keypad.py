
import RPi.GPIO as GPIO
from time import sleep
from pad4pi import rpi_gpio

#******************************************#
KEYPAD = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

#COL_PINS = [11, 7, 5, 3] # BOARD numbering
#ROW_PINS = [32,29,15,13] # BOARD numbering
COL_PINS = [17, 4, 3, 2] # BOARD numbering
ROW_PINS = [12,5,22,27] # BOARD numbering

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#******************************************#

def printKey(key):
  key=ord(key)
  if key==0x30:
    print("0")
  if key==0x31:
    print("1")
  if key==0x32:
    print("2")
  if key==0x33:
    print("3")
  if key==0x34:
    print("4")
  if key==0x35:
    print("5")
  if key==0x36:
    print("6")
  if key==0x37:
    print("7")
  if key==0x38:
    print("8")
  if key==0x39:
    print("9")
  if key==0x41:
    print("A")
  if key==0x42:
    print("B")
  if key==0x43:
    print("C")
  if key==0x44:
    print("D")
  if key==0x23:
    print("#")
  if key==0x2a:
    print("*")


#******************************************#

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

#******************************************#
def main():
  # Main program block
  global pm
  global system_sts
  
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  while True:
      sleep(1)

#******************************************#

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()

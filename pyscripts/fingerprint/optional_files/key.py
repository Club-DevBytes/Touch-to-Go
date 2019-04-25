from pad4pi import rpi_gpio
import time
import sys 

entered_passcode = ""
correct_passcode = "1234"


def processKey(key):
    print(key)
 
# Setup Keypad
KEYPAD = [
     ["1","2","3"],
     ["4","5","6"],
     ["7","8","9"],
     ["*","0","#"]
]
 
ROW_PINS = [11,23,24,25] # BCM numbering
COL_PINS = [17,27,22] # BCM numbering
 
factory = rpi_gpio.KeypadFactory()
 
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
 
a = keypad.registerKeyPressHandler(processKey)

def key_pressed(key):
    try:
        int_key = int(key)
        if int_key >= 0 and int_key <= 9:
            digit_entered(key)
    except ValueError:
        non_digit_entered(key)

def cleanup():
    global keypad
    keypad.cleanup()

try:
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_4_by_3_keypad() # makes assumptions about keypad layout and GPIO pin numbers

    keypad.registerKeyPressHandler(key_pressed)

    print("Enter your passcode (hint: {0}).".format(correct_passcode))
    print("Press * to clear previous digit.")

        
    while 1:
      time.sleep(1)
finally:
  cleanup()
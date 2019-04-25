from pad4pi import rpi_gpio
import time
import os

# Setup Keypad
KEYPAD = [
     ["1","2","3"],
     ["4","5","6"],
     ["7","8","9"],
     ["*","0","#"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
 
ROW_PINS = [11,23,24,25] # BCM numbering
COL_PINS = [17,27,22] # BCM numbering
 

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#keypad.cleanup()

def printKey(key):
  
  print(key)
  if (key=="1"):

 
    # disp.clear()
    # disp.display()
    # draw.rectangle((0,0,width,height), outline=0, fill=0)   
    # draw.text((x, top + 40),'Entering Enrollment' ,  font=font, fill=255)
    # disp.image(image)
    # disp.display()
    # time.sleep(2)
    print("hello")

  elif (key=='2'):
    print("helllo2")

  else:
    print("wrong input")

while 1:
# printKey will be called each time a keypad button is pressed
    keypad.registerKeyPressHandler(printKey)


try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()
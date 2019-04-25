from pad4pi import rpi_gpio
import time
 
# def processKey(key):
#     print(key)
#     return key
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


# ////////////////////////////

# global code 
code=''

def clear_keys():
  global code
  code = code.replace(code,'')




def doKey(key):

  global code 


    
	
    # code = ""
  code += key
  
  if key=='#':
      
      if code.endswith('#'):
        
        code = code[:-1]
  	    
        print(code)


print(code) 
  # clear_keys()
  

    
keypad.registerKeyPressHandler(doKey)

try:
	while(True):
		time.sleep(0.2)
except:
	keypad.cleanup()





























try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()
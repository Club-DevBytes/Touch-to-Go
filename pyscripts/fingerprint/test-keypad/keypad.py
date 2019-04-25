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
        #list to store them

    #function to clear string
class KeyStore():
    def __init__(self):
        #list to store them
        self.pressed_keys =''


    #function to clear string
    def clear_keys(self):
        self.pressed_keys = self.pressed_keys.replace(self.pressed_keys,'')

    def store_key(self,key):
        # self.key=key
        if key=='#':
            #printing the sequence of keys.
            
            print(self.pressed_keys)

            self.clear_keys()
            return self.pressed_keys


       
        
        else:
            self.pressed_keys += key
            # a=self.pressed_keys
    
    # def ret_Key(self,key):
    #     return key




# store_key will be called each time a keypad button is pressed

# keypad.registerKeyPressHandler( KeyStore().store_key)
obj1=KeyStore()
keypad.registerKeyPressHandler( KeyStore().store_key)
key_var=''


key_var=obj1.store_key('1')
print(key_var,'ADA')





#if a == "123":
#   print("hello")
# if keys.store_key == '123':
#   print("hello")

try:
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()
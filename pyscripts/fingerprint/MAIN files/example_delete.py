#!/usr/bin/env python
# -*- coding: utf-8 -*-



from pyfingerprint.pyfingerprint import PyFingerprint
import mysql.connector
import os
from pad4pi import rpi_gpio
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import RPi.GPIO as GPIO
import time
import sys
code=''
## Deletes a finger from sensor
##

RST = 0
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

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

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()


disp.clear()
disp.display()


width = disp.width
height = disp.height
image = Image.new('1', (width, height))


draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0


font = ImageFont.load_default()





mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="COMPANY"
)

mycursor = mydb.cursor()


try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')




except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))


def sql_delete(code) :

    sql1 = "SELECT SERIAL_NO FROM EMPLOYEE WHERE EMP_NO=" + str(code)

    mycursor.execute(sql1)

    myresult=mycursor.fetchall()
    # print(myresult)

    sr_no=myresult[0][0]

    

    sql="DELETE FROM EMPLOYEE WHERE EMP_NO=" + str(code)
    mycursor.execute(sql)


        #sql = "SELECT EMP_NO FROM EMPLOYEE WHERE SERIAL_NO=" + str(positionNumber)

        # val = (str(positionNumber))


        # mycursor.execute(sql)
    print('before chuspa' , type(sr_no), sr_no)
    sr_no = int(sr_no)
    print('after chuspa' , type(sr_no) , sr_no)
    
    mydb.commit()
    return sr_no



def doKey(key):

  global code 
  print('you are in dokey')  

    
	
    # code = ""
    
  code += key
  
  if key=='#':
      
      if code.endswith('#'):
        
        code = code[:-1]
  	    
        print(code) 
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)   
        draw.text((x, top + 5 ),        'Employee no. :' ,  font=font, fill=255)
        draw.text((x, top + 15),        code ,  font=font, fill=255)
        # draw.text((x, top + 36),        'Is the No. ok ?' ,  font=font, fill=255)
        draw.text((x, top + 25),        'press * to proceed' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        # time.sleep(2)
        keypad.registerKeyPressHandler(printKey)   #ye sirf key daal raha hai printkey mai joki dokey mai se aa raha hai
        print(code)



def printKey(key):
  
  print(key)
  global code
  if (key=="*"):
    if code.endswith('*'):
        code = code[:-1]
        # sql_delete(code)
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, top + 26),        'Employee Number:' ,  font=font, fill=255)
        draw.text((x, top + 36),       code  ,  font=font, fill=255)
        draw.text((x, top + 46),        'Employee deleted' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        GPIO.cleanup()
        time.sleep(1)
  
        ## Tries to delete the template of the finger
        # positionNumber = 0
        try:
            positionNumber = int(sql_delete(code))

            # positionNumber = 0
            # print(type(code), code)
            # sql_trial=sql_delete(code)
            # print(' this is fucking sql' , sql_trial)
            
            # positionNumber = int(positionNumber)
            print('this is ' , positionNumber)

            if ( f.deleteTemplate(positionNumber) == True ):
                print('Employee deleted!')
                os.system('python ~/Desktop/fingerprint/main.py')



        # sql_delete(emp_no)



        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)




# def sql_delete(code) :

#     sql1 = "SELECT SERIAL_NO FROM EMPLOYEE WHERE EMP_NO=" + str(code)

#     mycursor.execute(sql1)

#     myresult=mycursor.fetchall()
#     # print(myresult)

#     sr_no=myresult[0][0]

#     print(sr_no)





#     sql="DELETE FROM EMPLOYEE WHERE EMP_NO=" + str(code)
#     mycursor.execute(sql)


#         #sql = "SELECT EMP_NO FROM EMPLOYEE WHERE SERIAL_NO=" + str(positionNumber)

#         # val = (str(positionNumber))


#         # mycursor.execute(sql)

#     mydb.commit()
#     return sr_no

disp.clear()
disp.display()
draw.rectangle((0,0,width,height), outline=0, fill=0)   
draw.text((x, top + 5),       'enter employee' ,  font=font, fill=255)
draw.text((x, top + 15),        'no:' ,  font=font, fill=255)
draw.text((x, top + 25),        'Press # after' ,  font=font, fill=255)
draw.text((x, top + 35),        'Completion' ,  font=font, fill=255)

disp.image(image)
disp.display()
keypad.registerKeyPressHandler(doKey)
time.sleep(1000000)
 


## Tries to initialize the sensor
# try:
#     f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

#     if ( f.verifyPassword() == False ):
#         raise ValueError('The given fingerprint sensor password is wrong!')




# except Exception as e:
#     print('The fingerprint sensor could not be initialized!')
#     print('Exception message: ' + str(e))
#     exit(1)

# ## Gets some sensor information
# print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

# ## Tries to delete the template of the finger
# try:
#     positionNumber = sql_delete(code)
#     positionNumber = int(positionNumber)
#     print('this is ' , positionNumber)

#     if ( f.deleteTemplate(positionNumber) == True ):
#         print('Employee deleted!')
#         os.system('python ~/Desktop/fingerprint/main.py')



# # sql_delete(emp_no)



# except Exception as e:
#     print('Operation failed!')
#     print('Exception message: ' + str(e))
#     exit(1)

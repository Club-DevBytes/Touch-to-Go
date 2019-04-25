#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from pyfingerprint.pyfingerprint import PyFingerprint
import json
import os
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
import datetime
import RPi.GPIO as GPIO
import mysql.connector
from pad4pi import rpi_gpio


code=''

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
    host="127.0.0.1",
    user="root",
    passwd="",
    database="COMPANY"
)

mycursor = mydb.cursor()



def printKey(key):
  global code
  print(key)
  if (key=="*"):
    if code.endswith('*'):
        code = code[:-1]
        sql_enroll(code, positionNumber)
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, top + 26),        'Employee Number:' ,  font=font, fill=255)
        draw.text((x, top + 36),       code  ,  font=font, fill=255)
        draw.text((x, top + 46),        'Employee add suceess' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        GPIO.cleanup()
        time.sleep(2)
        os.system("python ~/Desktop/fingerprint/main.py")  
#   elif (key == "*"):
#     disp.clear()
#     disp.display()
#     draw.rectangle((0,0,width,height), outline=0, fill=0)
#     draw.text((x, top + 26),        'Good Bye' ,  font=font, fill=255)
#     disp.image(image)
#     disp.display()
#     time.sleep(2)
#     os.system("python ~/Desktop/fingerprint/main.py")
#   else :
#     disp.clear()
#     disp.display()
#     draw.rectangle((0,0,width,height), outline=0, fill=0)
#     draw.text((x, top + 26),        'Wrong Input' ,  font=font, fill=255)
#     disp.image(image)
#     disp.display()
#     time.sleep(2)
#     os.system("python ~/Desktop/fingerprint/main.py") 
def sql_enroll(code ,positionNumber):

    
    
    
    
    sql = "INSERT INTO EMPLOYEE (SERIAL_NO, EMP_NO) VALUES (%s, %s)"
    val = (str(positionNumber),str(code))
    mycursor.execute(sql, val)

    mydb.commit()
    

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
        # time.sleep(1)
        keypad.registerKeyPressHandler(printKey)   
## Enrolls new finger
##

## Tries to initialize the sensor
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

## Tries to enroll new finger
while 1:
    draw.text((x, top + 10),       'Welcome to Enroll' ,  font=font, fill=255)
    draw.text((x, top + 35),       'Waiting for finger...' ,  font=font, fill=255)
    print('Waiting for finger...')
    disp.image(image)
    disp.display()
    time.sleep(.1)


    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    ## Checks if finger is already enrolled
    result = f.searchTemplate()
    positionNumber = result[0]

    if ( positionNumber >= 0 ):
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)   
        draw.text((x, top + 40),'Finger already exists' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(1)

        print('Template already exists at position #' + str(positionNumber))
        os.system("python ~/Desktop/fingerprint/main.py")
    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top + 40),       'Remove finger' ,  font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(.1)
    print('Remove finger...')
    time.sleep(2)

    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
   
    draw.text((x, top + 35),       'Waiting for same' ,  font=font, fill=255)
    draw.text((x, top + 43),       'finger again' ,  font=font, fill=255)
    disp.image(image)
    disp.display()
    

    print('Waiting for same finger again...')
    time.sleep(.1)

    ## Wait that finger is read again
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 2
    f.convertImage(0x02)

    ## Compares the charbuffers
    if ( f.compareCharacteristics() == 0 ):
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)   
        draw.text((x, top + 35),       'Fingers do not match' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(2)
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)   
        os.system("python ~/Desktop/fingerprint/main.py")

    ## Creates a template
    f.createTemplate()



    ## Saves template at new position number
    positionNumber = f.storeTemplate()

    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)   
    draw.text((x, top + 5),       'Please enter employee' ,  font=font, fill=255)
    draw.text((x, top + 15),        'no:' ,  font=font, fill=255)
    draw.text((x, top + 25),        'Press # after' ,  font=font, fill=255)
    draw.text((x, top + 35),        'Copletion' ,  font=font, fill=255)
 
    disp.image(image)
    disp.display()
    keypad.registerKeyPressHandler(doKey)
    time.sleep(10000000)
 
    


# print(type(code))

    
     
    
    
    
    
    # disp.clear()
    # disp.display()
    # draw.rectangle((0,0,width,height), outline=0, fill=0)   
    # draw.text((x, top + 16),        'Employee no. :' ,  font=font, fill=255)
    # draw.text((x, top + 26),        str(emp_no) ,  font=font, fill=255)
    # # draw.text((x, top + 36),        'Is the No. ok ?' ,  font=font, fill=255)
    # draw.text((x, top + 46),        'press # to proceed' ,  font=font, fill=255)
    # disp.image(image)
    # disp.display()
    # keypad.registerKeyPressHandler(printKey)
    # time.sleep(1000000)
    # while 1:
        
        # time.sleep(100000)
        # if  ans1 == str(ans):
        #     disp.clear()
        #     disp.display()
        #     draw.rectangle((0,0,width,height), outline=0, fill=0)
        #     draw.text((x, top + 26),        'Employee Number:' ,  font=font, fill=255)
        #     disp.image(image)
        #     disp.display()


    # sql_enroll(emp_no, positionNumber)

        #     draw.text((x, top + 32),        'Employee added suceessfully' ,  font=font, fill=255)
        #     GPIO.cleanup()  
        #     break
        # else:
        #     disp.clear()
        #     disp.display()
        #     draw.rectangle((0,0,width,height), outline=0, fill=0)   
        #     draw.text((x, top + 24),       'Please enter employee' ,  font=font, fill=255)
        #     draw.text((x, top + 32),        'no:' ,  font=font, fill=255)
        #     disp.image(image)
        #     disp.display()
        #     emp_no = raw_input("What is your Employ NO:? ")
        #     disp.clear()
        #     disp.display()
        #     draw.rectangle((0,0,width,height), outline=0, fill=0)   
        #     draw.text((x, top + 16),        'Employee No:' ,  font=font, fill=255)
        #     draw.text((x, top + 26),        str(emp_no) ,  font=font, fill=255)
        #     draw.text((x, top + 36),        'Is the no. ok ?' ,  font=font, fill=255)
        #     draw.text((x, top + 46),        'press y if : yes' ,  font=font, fill=255)
        #     draw.text((x, top + 56),        'press n if : no' ,  font=font, fill=255)
        #     disp.image(image)
        #     disp.display()
        #     os.system("python ~/Desktop/fingerprint/main.py")



    




    # disp.clear()
    # disp.display()
    # draw.rectangle((0,0,width,height), outline=0, fill=0)   
    # draw.text((x, top + 35),       'Employee Added SucessFully!' ,  font=font, fill=255)
    # disp.image(image)
    # disp.display()

  



#     def append_record(record):
#         with open('my_file', 'a') as f:
#             json.dump(record, f)
#             f.write(os.linesep)

# # demonstrate a program writing multiple records
#     my_dict = {positionNumber:name}
#     append_record(my_dict)

    
    # disp.clear()
    # disp.display()
    # draw.rectangle((0,0,width,height), outline=0, fill=0)   
    # draw.text((x, top + 24),       'Employee Added Sucess ' ,  font=font, fill=255)
    # disp.image(image)
    # disp.display()
    # time.sleep(2)
    # os.system("python ~/Desktop/fingerprint/main.py")
    # print('Finger enrolled successfully!')
    # print('New template position #' + str(positionNumber))






# CREATE TABLE EMPLOYEE (NAME VARCHAR(255), EMP_NO VARCHAR(255), SERIAL_NO VARCHAR(255))

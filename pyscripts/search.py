#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import json

import datetime
import time
from time import sleep, strftime
import mysql.connector
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
import os
from pad4pi import rpi_gpio
import webbrowser
import subprocess
import sys
import RPi.GPIO as GPIO
# import cloudinary
# import cloudinary.uploader
# import glob
GPIO.setwarnings(False)

# BaseDirectory = '/home/pi/pimage/'



 


# cloudinary.config( 
#   cloud_name = "dvey2m05b", 
#   api_key = "973346668589726", 
#   api_secret = "fH8IA-L48NbxnhrVQUz8utXMuJg" 
# )

KEYPAD = [
     ["1","2","3"],
     ["4","5","6"],
     ["7","8","9"],
     ["*","0","#"]
]


# def cloudinaryUpload(imgPath):
#         resp =  cloudinary.uploader.upload(imgPath)
#         url = resp["secure_url"]
#         print(url)
#         return url



# def latestFile():
#         list_of_files = glob.glob(BaseDirectory + '*') # * means all if need specific format then *.csv
#         latest_file = max(list_of_files, key=os.path.getctime)
#         print (latest_file)
#         return latest_file




ROW_PINS = [11,23,24,25] # BCM numbering
COL_PINS = [17,27,22] # BCM numbering
 
factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)


RST = 0
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
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
    passwd="root",
    database="COMPANY"
)

mycursor = mydb.cursor()


def sql_update(Emp_no):

    time = datetime.datetime.now().strftime ("%H:%M:%S")
    date = datetime.datetime.now().strftime ("%Y-%m-%d")

    sql = "SELECT * FROM ATTENDENCE WHERE SERIAL_NO = %s AND DATE= %s AND OUT_TIME is null"
    val = (str(positionNumber), date)

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    print(myresult)

    tick = len(myresult)
    
    if tick:

        sql = "UPDATE ATTENDENCE SET OUT_TIME = %s WHERE SERIAL_NO = %s AND DATE= %s AND OUT_TIME is null"
        val = (time, str(positionNumber), date)

        mycursor.execute(sql, val)

        mydb.commit()

        

    if not tick:
        
        sql = "INSERT INTO ATTENDENCE (SERIAL_NO,EMP_ID, DATE, IN_TIME) VALUES (%s,%s, %s, %s)"
        val = (str(positionNumber), str(Emp_no),date, time )
        mycursor.execute(sql, val)

        mydb.commit()
    

# def updateINPIC(in_pic,emp_id):
  

#     sql = "UPDATE ATTENDENCE SET IN_PIC = %s WHERE EMP_ID"
#     val = (in_pic, emp_id)

#     mycursor.execute(sql, val)
#     mydb.commit()

# def updateOUTPIC(out_pic,emp_id):
    

#     sql = "UPDATE ATTENDENCE SET OUT_PIC = %s WHERE EMP_ID = %s"
#     val = (out_pic, emp_id)

#     mycursor.execute(sql, val)
#     mydb.commit()


def sql_extract(positionNumber):

    sql = "SELECT EMP_NO FROM EMPLOYEE WHERE SERIAL_NO=" + str(positionNumber)



    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    print(myresult)

    emp_no = myresult[0][0]

    print(emp_no)

    return emp_no
def printKey(key):
  print(key)
  if (key=="#"):
    # webbrowser.open('http://127.0.0.1:8887/attend.html', new=0, autoraise=True)
    
    sql_update(Emp_No)
    while 1:  
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)   
        draw.text((x, top ),    str(Emp_No)    ,  font=font, fill=255)
        draw.text((x, top + 8),       'Attendance Done' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        os.system("python ~/Desktop/GIH/search.py")
    # python_bin = "/home/pi/python-virtual-environments/env1/bin/python3"
    # script_file = "/home/pi/Desktop/fingerprint/test.py"
    # subprocess.Popen([python_bin, script_file])
    
  elif (key == "*") :
    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)   
    draw.text((x, top ),    str(Emp_No)    ,  font=font, fill=255)
    draw.text((x, top + 16),       ' OK, YOU CAN LEAVE!' ,  font=font, fill=255)
    disp.image(image)
    disp.display()
    print(Emp_No)
    print("Ok You can Leave?")
    os.system("python ~/Desktop/GIH/search.py")
    # elif (key == "5") :
    #     disp.clear()
    #     disp.display()
    #     draw.rectangle((0,0,width,height), outline=0, fill=0)   
    #     draw.text((x, top ),    str(Emp_No)    ,  font=font, fill=255)
    #     draw.text((x, top + 16),       'Welcome Admin!' ,  font=font, fill=255)
    #     disp.image(image)
    #     disp.display()
    #     print(Emp_No)
    #     print("Ok You can Leave?")
    #     os.system("python3 ~/Desktop/GIH/fingerprint/main.py") 
  else :
    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)   
    draw.text((x, top ),    str(Emp_No)    ,  font=font, fill=255)
    draw.text((x, top + 16),       ' Incorrect input!' ,  font=font, fill=255)
    disp.image(image)
    disp.display()
    print(Emp_No)
    print("Incorrect input")
    os.system("python ~/Desktop/GIH/search.py")  

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    os.system("python search.py")

print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

while 1:
    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top),       'Waiting for finger...' ,  font=font, fill=255)
    draw.text((0, top + 20), strftime('%a, %b %d %Y'), font=font, fill=1)
    print('Waiting for finger...')
    disp.image(image)
    disp.display()
    print("Waiting for Finger")
    
    while ( f.readImage() == False ):
        pass

    
    f.convertImage(0x01)   
    f.createTemplate()
    temp = f.createTemplate()
    






    result = f.searchTemplate()

    positionNumber = result[0]
    
    if ( positionNumber == -1 ):
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, top),       'No match found' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        print('No match found!')
        os.system("python ~/Desktop/GIH/search.py")
        exit(0)
    else:
        print('Found template at position #' + str(positionNumber))
       
        Emp_No = sql_extract(positionNumber)
        # os.system('fswebcam -r 1280x720 --no-banner ~/pimage/'+ Emp_No + '.jpg')
        # cloud_url=cloudinaryUpload(latestFile())
        webbrowser.open("/home/pi/Desktop/GIH/fingerprint/hello.mp3")
       
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)   
        draw.text((x, top),        'Are You Sure!' ,  font=font, fill=255)
        draw.text((x, top + 10),        'press # if : yes' ,  font=font, fill=255)
        draw.text((x, top + 20),        'press * if : no' ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        print("# if : Yes")
        print("* if: NO")
        keypad.registerKeyPressHandler(printKey)
        time.sleep(1000000)
       
    f.loadTemplate(positionNumber, 0x01)

   
    characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

   

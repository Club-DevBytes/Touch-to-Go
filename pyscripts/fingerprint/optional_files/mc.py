import os
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import subprocess

from pad4pi import rpi_gpio

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# KEYPAD = [
#      ["1","2","3"],
#      ["4","5","6"],
#      ["7","8","9"],
#      ["*","0","#"]
# ]

# ROW_PINS = [11,23,24,25] # BCM numbering
# COL_PINS = [17,27,22] # BCM numbering

# factory = rpi_gpio.KeypadFactory()

# keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)



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

# def printKey(key):
  
#   print(key)
#   if (key=="1"):
#     disp.clear()
#     disp.display()
#     draw.rectangle((0,0,width,height), outline=0, fill=0)   
#     draw.text((x, top + 40),'Entering Enrollment' ,  font=font, fill=255)
#     disp.image(image)
#     disp.display()
#     time.sleep(2)
#     os.system("python ~/Desktop/fingerprint/enroll_trial.py")
#     print("Going to Enroll")
#   elif (key =="2"):
#     disp.clear()
#     disp.display()
#     draw.rectangle((0,0,width,height), outline=0, fill=0)   
#     draw.text((x, top + 40),'Entering Attendance' ,  font=font, fill=255)
#     disp.image(image)
#     disp.display()
#     time.sleep(2)
#     os.system("python ~/Desktop/fingerprint/search.py") 
#     print("Going to Attendance")
#   elif (key == "3"):
#     disp.clear()
#     disp.display()
#     draw.rectangle((0,0,width,height), outline=0, fill=0)   
#     draw.text((x, top + 40),'Entering Delete' ,  font=font, fill=255)
#     disp.image(image)
#     disp.display()
#     time.sleep(2)
#     os.system("python ~/Desktop/fingerprint/example_delete.py") 
#     print("Going to Delete")
#   else :
#     disp.clear()
#     disp.display()
#     draw.rectangle((0,0,width,height), outline=0, fill=0)   
#     draw.text((x, top + 40),'Wrong Input' ,  font=font, fill=255)
#     disp.image(image)
#     disp.display()
#     time.sleep(2)
#     print("wrong input")
while 1:
  print("Welcome To Das InfoMedia!\n")
  print("Press 1 for Enroll : \n")
  print("Press 2 for Search : \n")
  print("Press 3 for delete : \n")
  disp.begin()


  disp.clear()
  disp.display()
  draw.rectangle((0,0,width,height), outline=0, fill=0)   
  draw.text((x, top),'Welcome to ' ,  font=font, fill=255)
  draw.text((x, top + 10),'Das InfoMedia!' ,  font=font, fill=255)
  draw.text((x, top + 30),'Press 1 for Enroll :' ,  font=font, fill=255)
  draw.text((x, top + 40 ),'Press 2-Attendance:' ,  font=font, fill=255)
  draw.text((x, top + 50),'Press 3 for Delete :' ,  font=font, fill=255)
  disp.image(image)
  disp.display()
  time.sleep(100000)
# keypad.registerKeyPressHandler(printKey)

    # if ans1 == str(ans) :
    #     print("Enter password: ")
    #     disp.clear()
    #     disp.display()
    #     draw.rectangle((0,0,width,height), outline=0, fill=0)   
    #     draw.text((x, top + 40),'Enter password: ' ,  font=font, fill=255)
    #     disp.image(image)
    #     disp.display()
    #     time.sleep(.1)
    #     pass_word = raw_input("Password comparing")

    #     pass_word1 = '12345'
    #     if pass_word1 == str(pass_word) :
    #         disp.clear()
    #         disp.display()
    #         draw.rectangle((0,0,width,height), outline=0, fill=0)   
    #         draw.text((x, top + 40),'Password Correct' ,  font=font, fill=255)
    #         draw.text((x, top + 50),'Entering Enrollment' ,  font=font, fill=255)
    #         disp.image(image)
    #         disp.display()
    #         time.sleep(2)
    #         os.system("python ~/Desktop/fingerprint/example_enroll.py")
    #     else :
    #         print("Wrong Pass")
    #         disp.clear()
    #         disp.display()
    #         draw.rectangle((0,0,width,height), outline=0, fill=0)   
    #         draw.text((x, top + 40),'Password unCorrect' ,  font=font, fill=255)
    #         draw.text((x, top + 50),'Please Try Again' ,  font=font, fill=255)
    #         disp.image(image)
    #         disp.display()
    #         time.sleep(2)
    # elif ans2 == str(ans) :
    #         disp.clear()
    #         disp.display()
    #         draw.rectangle((0,0,width,height), outline=0, fill=0)   
    #         draw.text((x, top + 40),'Going Search Script' ,  font=font, fill=255)
    #         disp.image(image)
    #         disp.display()
    #         time.sleep(2)
    #         os.system("python ~/Desktop/fingerprint/search.py")

    # elif ans3 == str(ans) :
    #     print("Enter password")
    #     pass_word = raw_input("Password comparing :")

    #     pass_word1 = '12345'
    #     if pass_word1 == str(pass_word) :
    #         disp.clear()
    #         disp.display()
    #         draw.rectangle((0,0,width,height), outline=0, fill=0)   
    #         draw.text((x, top + 40),'Password Correct' ,  font=font, fill=255)
    #         draw.text((x, top + 50),'Going Delete Script' ,  font=font, fill=255)
    #         disp.image(image)
    #         disp.display()
    #         time.sleep(2)
    #         os.system("python ~/Desktop/fingerprint/example_delete.py")
    #     else :
    #         disp.clear()
    #         disp.display()
    #         draw.rectangle((0,0,width,height), outline=0, fill=0)   
    #         draw.text((x, top + 40),'Password inCorrect' ,  font=font, fill=255)
    #         draw.text((x, top + 50),'Please Try Again' ,  font=font, fill=255)
    #         disp.image(image)
    #         disp.display()
    #         time.sleep(2)
    #         print("Wrong Pass")
    # else :
   

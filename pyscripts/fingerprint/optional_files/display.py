import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

RST = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image1 = Image.new('1', (width, height))
draw = ImageDraw.Draw(image1)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Write two lines of text.
    disp.clear()
    disp.display()
    draw.text((x, top),       'OLED Interfacing ' ,  font=font, fill=255)
    draw.text((x, top+8),     "Circuit Digest", font=font, fill=255)
    draw.text((x, top+16),    "For more Videos",  font=font, fill=255)
    draw.text((x, top+25),    "Visit at",  font=font, fill=255)
    draw.text((x, top+34),    "www.circuitdigest.com",  font=font, fill=255)

    # Display image.
    disp.image(image1)
    disp.display()
    time.sleep(2)

    if disp.height == 64:
        image = Image.open('img1.png').convert('1')
    else:
        image = Image.open('img1.png').convert('1')

    disp.image(image)
    disp.display()
    time.sleep(2)

    if disp.height == 64:
        image = Image.open('img3.jpg').convert('1')
    else:
        image = Image.open('img3.jpg').convert('1')

    disp.image(image)
    disp.display()
    time.sleep(2)

    if disp.height == 64:
        image = Image.open('img4.jpg').convert('1')
    else:
        image = Image.open('img4.jpg').convert('1')

    disp.image(image)
    disp.display()
    time.sleep(2)
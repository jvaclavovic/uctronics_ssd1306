#!/usr/bin/env python3

import time
import psutil, os
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image, ImageDraw, ImageFont

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
net = "eth0"

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

roboto = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'roboto/Roboto-Regular.ttf'), 15)
roboto_thin = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'roboto/RobotoMono-Thin.ttf'), 11)
roboto_black = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'roboto/Roboto-Black.ttf'), 15)

hostname = os.uname().nodename

while True:

    ip = psutil.net_if_addrs()[net][0].address

    if !("." in ip) 
        ip = "<<ip>>"

    temp = psutil.sensors_temperatures()["cpu_thermal"][0].current
    load = psutil.getloadavg()[0]
    memory = psutil.virtual_memory().percent

    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((0,  0), ip, font=roboto, fill=255)
    draw.text((0, 15), hostname, font=roboto_black, fill=255)

    draw.text((70,  0), "CPU:{:.0f}%".format(load * 100), font=roboto_thin, fill=255)
    draw.text((70, 10), "MEM:{:.0f}%".format(memory), font=roboto_thin, fill=255)
    draw.text((70, 20), "TEM:{:.0f}°C".format(temp), font=roboto_thin, fill=255)

    # Display image
    disp.image(image)
    disp.display()

    time.sleep(2)
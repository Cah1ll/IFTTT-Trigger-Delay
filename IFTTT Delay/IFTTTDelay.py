#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
import time
import calendar
import requests
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from datetime import datetime

epd = epd2in13_V2.EPD()                                         #Set the display

HBlackImage = Image.new('1', (epd.height, epd.width), 255)      #Create Blank image
draw = ImageDraw.Draw(HBlackImage)                              #Create draw image

epd.init(epd.FULL_UPDATE)                                       #Initialize Full update
print("Clear...")
epd.displayPartBaseImage(epd.getbuffer(HBlackImage))            #Draw Blank image to screen to "clear" data

epd.init(epd.PART_UPDATE)                                       #Initialize Partial Updates
font = ImageFont.truetype("FreeMono.ttf", 35)
font2 = ImageFont.truetype("FreeMono.ttf", 25)

indelay = input("Enter Delay in Mins: ")

#*****************EVENT1*****************
requests.post('https://maker.ifttt.com/trigger/"EVENT""/with/key/""IFTTTKEY"')  #*****Replace EVENT and IFTTTKEY with IFTTT credentials NO QUOTES


delay = indelay * 60
iDelay = delay
i = 0
j = 0
while (i<=delay):
   vDelay = time.strftime('%M:%S', time.gmtime(iDelay))
   draw.rectangle((0, 0, epd.height, epd.width), fill = 255)      #Needed to for inbetween refreshes
   draw.text((30,15),"UV Light On",font = font2, fill = 0)
   draw.text((60, 45),vDelay, font = font, fill = 0)
   epd.displayPartial(epd.getbuffer(HBlackImage))
   i += 1
   iDelay -= 1
#Refresh display after 90 seconds to avoid ghosting
   if (j == 90):
       epd.init(epd.FULL_UPDATE)                                       #Initialize Full update
       print("Refreshing...")
       epd.displayPartBaseImage(epd.getbuffer(HBlackImage))
       epd.init(epd.PART_UPDATE)
       j = 0
       iDelay -= 4  #<<<<********************Replace 4 with the amount of time it takes for deplay to update (seconds)**************
       delay -= 4   #<<<<********************Replace 4 with the amount of time it takes for deplay to update (seconds)**************

#*****************EVENT2*****************
requests.post('https://maker.ifttt.com/trigger/"EVENT""/with/key/""IFTTTKEY"')  #*****Replace EVENT and IFTTTKEY with IFTTT credentials NO QUOTES

draw.rectangle((0, 0, epd.height, epd.width), fill = 255)      #Needed to for inbetween refreshes
draw.text((27, 20),"UV Curing", font = font, fill = 0)
draw.text((34, 55),"Complete", font = font, fill = 0)
epd.displayPartial(epd.getbuffer(HBlackImage))

print("Display Updated")
epd.sleep()                                                     #Display put to sleep
print("Display Asleep")

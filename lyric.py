#!/usr/bin/python
# -*- coding:utf-8 -*-















import sys
sys.path.append('.')
import epd7in5
from PIL import Image,ImageDraw,ImageFont
import traceback
from PyLyrics import *
from time import *


def playlyrics(inp):
    parsinp = inp.split(' by ')
    lyricfull = (PyLyrics.getLyrics(parsinp[1],parsinp[0]))
    lyriclist = lyricfull.split('\n')
    try:
        epd = epd7in5.EPD()
        epd.init()
        print("Clear")
        epd.Clear(0xFF)

        print("Drawing")
        Himage = Image.new('1', (epd7in5.EPD_WIDTH, epd7in5.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(Himage)
        font24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 24)
        for x in range (0, 4, len(lyriclist)-1):
            draw.text((10, x*20), lyriclist[x], font = font24, fill = 0)
            draw.text((10, (x+1)*20), lyriclist[x+1], font = font24, fill = 0)
            draw.text((10, (x+2)*20), lyriclist[x+2], font = font24, fill = 0)
            epd.display(epd.getbuffer(Himage))
            sleep(1)
        epd.display(epd.getbuffer(Himage))
        sleep(2)

        epd.sleep()
    except:
        print('traceback.format_exc():\n%s', traceback.format_exc())
        exit()





#------Main-----
playlyrics('Otherside by Post Malone')



#parsinp = inp.split(' by ')
#lyricfull = (PyLyrics.getLyrics(parsinp[1],parsinp[0]))

#lyriclist = lyricfull.split('\n')

'''for x in range(0, len(lyriclist)-1):
    print(lyriclist[x])
    sleep(1)
'''



'''try:
    epd = epd7in5.EPD()
    epd.init()
    print("Clear")
    epd.Clear(0xFF)

    print("Drawing")
    # Drawing on the Horizontal image
    Himage = Image.new('1', (epd7in5.EPD_WIDTH, epd7in5.EPD_HEIGHT), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(Himage)
    font24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 24)
    for x in range(0,3,len(lyriclist)-1):
        draw.text((10, x*20 ), lyriclist[x], font = font24, fill = 0)
        draw.text((10, (x+1)*20), lyriclist[x+1], font = font24, fill = 0)
        draw.text((10, (x+2)*20), lyriclist[x+2], font = font24, fill = 0)
        #print(lyriclist[x])
        epd.display(epd.getbuffer(Himage))
        sleep(1) 


    epd.display(epd.getbuffer(Himage))
    sleep(2)
        
    epd.sleep()
            
except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
'''

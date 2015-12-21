#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pillow: python imaging library
PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
"""

from PIL import Image, ImageDraw, ImageFont

original_avatar = 'weChat_avatar.png'
saved_avatar = 'new_avatar.jpg'
windows_font = 'Arial.ttf'
color = (255, 0, 0)

def draw_text(text, fill_color, windows_font):
    try:
        im = Image.open(original_avatar)
        x, y = im.size
        print "The size of Image is: "
        print(im.format, im.size, im.mode)
        im.show()
    
        draw = Image.Draw.Draw(im)
        font = ImageFont.truetype(windows_font, 35)
        draw.text((x-20, 7), text, fill_color, font)
        
        im.save(saved_avatar)
        im.show()
        
    except:
        print "Unable to load image"
        
if __name__ == "__main__":
    number = str(4)
    draw_text(number, color, windows_font)

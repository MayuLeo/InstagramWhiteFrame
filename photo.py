#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import sys
import os
args = sys.argv


width = 1080
height = 720
if not os.path.exists("./white"):
	os.mkdir("./white")
for photo in args[1:]:
	print(photo[-12:])
	img = Image.open(str(photo))
	img.thumbnail((width,height),Image.ANTIALIAS)
	
	bg = Image.new("RGB",[width,width],(255,255,255))
	
	bg.paste(img,(int((width-img.size[0])/2),180))
	
	bg.save("./white/" + str(photo[-12:]),quality=100)

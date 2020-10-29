# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:20:31 2019

@author: joshu
"""


#!/usr/bin/python
from PIL import Image
import os, sys

path = "C:\\Users\\joshu\\OneDrive\\Desktop\\MachineLearningPython\\Fish"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((224,224), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', 'png', quality=90)

resize()
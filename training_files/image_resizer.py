"""
Change the value of fx and fx to get required size
Put this code in the directory of images and run it
"""

import numpy as np
import cv2
import os

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    if filename.endswith(".jpg"):
        image = cv2.imread(filename)
        resized = cv2.resize(image,None,fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename,resized)
    print filename, '--> resized !'

print 'Completed!

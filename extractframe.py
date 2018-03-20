# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:15:20 2018

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:31:56 2018

@author: Pratiksha
"""

import cv2
import os
import imutils

print(cv2.__version__)
vidcap = cv2.VideoCapture('asd.mp4')
success,image = vidcap.read()
count = 0
folder='F:\\sign-language-alphabet-recognizer-master\\temp\\'
success = True
while success:
  success,image = vidcap.read()
  if(count%30==0):
      rotated = imutils.rotate_bound(image, 90)
      cv2.imwrite("frame%d.jpg" % count, rotated)     # save frame as JPEG file
      cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), rotated) 
      
      #print ('Read a new frame: ', success)
  
  count += 1

  print(count)

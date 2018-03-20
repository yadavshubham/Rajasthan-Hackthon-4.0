# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:53:04 2018

@author: Ghanshyam :-)
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
r, h, c, w = 50, 350, 125, 250
track_hand = (c, r, w, h)
roi = frame[r:r + h, c:c + w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
#cv2.imwrite("output/crop{}_{}.jpg".format(pic, cnt), imgCrop)

# Setup the termination criteria, either 10 iteration or move by atleas1t 
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while (1):
    ret, frame = cap.read()
    cnt =0
    
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        ret, track_hand = cv2.meanShift(dst, track_hand, term_crit)
        
        x, y, w, h = track_hand
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0, 0), 2)
        dst = np.zeros_like(frame)
        dst[y:y+h,x:x+w] = frame[y:y+h,x:x+w]
        ###for i in range(1, 200):
        ###    if(i%3==0):
        ###     cv2.imwrite("crop{}_{}.jpg".format(i,cnt),dst)
        ###     cnt += 1
        cv2.imshow('dst',dst)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
    else:
        break
    

cv2.destroyAllWindows()
cap.release()

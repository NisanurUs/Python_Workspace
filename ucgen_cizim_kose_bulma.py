# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:13:03 2024

@author: usnis
"""

#Bu kod, bir tuval oluşturur ve üzerinde bir üçgen çizer. Ardından, çizilen üçgenin köşelerini tespit eder ve bu köşeleri vurgular. 
# Tuval oluşturma: Beyaz arka plan.
# Üçgen çizme: Belirtilen koordinatlarla.
# Köşeleri tespit etme: `cv2.goodFeaturesToTrack` fonksiyonu kullanarak.


import cv2
import numpy as np


w, h= 640,480

canvas=np.ones((h,w,3), dtype=np.uint8)*255 # "zerosda + "   "ones da *"

triangle=np.array([[200,100],[400,100],[300,300]])


cv2.polylines(canvas, [triangle], isClosed=True, color=(255,0,0), thickness=2)

gray=cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray, maxCorners=3, qualityLevel=0.01, minDistance=10)
corners=np.int64(corners)

for corner in corners:
    x,y =corner.ravel()
    cv2.circle(canvas, (x,y), 5, (0,0,255),3)

cv2.imshow("win", canvas)

cv2.waitKey()
cv2.destroyAllWindows()
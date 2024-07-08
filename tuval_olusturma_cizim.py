# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:49:52 2024

@author: usnis
"""

#tuval penceresi oluşturma
#Bu kod, bir resim dosyasını yükler ve bu resmi farklı renk uzaylarına (RGB, HSV, Gri) dönüştürür. Orijinal ve dönüştürülmüş resimleri görüntüler.


import cv2
import numpy as np

width, heigth =640, 480

canvas = np.zeros((width, heigth, 3), dtype= np.uint8 ) +223 #+255 -> beyaz canvas, eğer yazmazsak siayh , uint8 256 ya kadar değer alır renk skalasıdır 


cv2.line(canvas, (0,75), (640,75), (0,0,0), 3) #tuval, başlangı. koordinat, bitiş koordinat, renk, kalınlık
cv2.rectangle(canvas, (100,100),(250,200), (0,0,215),-1) #-1 içini dolduruyor
cv2.circle(canvas, (400,400), 50, (100,200,100), -1)

cv2.putText(canvas, "Mavi", (100,300), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX , 2, (0,0,0), 2)

cv2.imshow("window", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()


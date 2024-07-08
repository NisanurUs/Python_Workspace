# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:17:40 2024

@author: usnis
"""
#Bu kod, varsayılan web kamerasını kullanarak bir kare yakalar ve bu kareyi belirtilen yola kaydeder. Yakalanan kareyi bir pencerede görüntüler.

import cv2

save_path="ss.jpg"

cap=cv2.VideoCapture(0)  # kamera yakalama 0 varsayılan web cam

ret, frame =cap.read()  # frame i yakalayıp okuma işleöi t or f döner 

if ret:
    cv2.imshow("pencere", frame)
    
    cv2.waitKey(0)
    cv2.imwrite(save_path, frame) 
    
    
else:
    print("kamera açılmadı...")
    

cap.release()   #kamerayı serbest bırakmak için
cv2.destroyAllWindows()

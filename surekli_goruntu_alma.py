# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:39:20 2024

@author: usnis
"""

#kameradan sürekli görüntü alma
#Bu kod, varsayılan web kamerasından sürekli olarak görüntü alır ve bu görüntüleri bir pencerede gösterir. 'q' tuşuna basılarak görüntü almayı sonlandırır.


import cv2

cap=cv2.VideoCapture(0)  # 0 yerine açılacak videonun path yazılırsa onu oynatır


while True:
    ret, frame =cap.read()
    
    if not ret:
        break
    
    cv2.imshow("window", frame)
    
    if cv2.waitKey(5) & 0xFF==ord("q"):  # q ile sonlandır görüntü almayı
        break
    
    
    
    
cap.release()
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:26:36 2024

@author: usnis
"""
#u kod, OpenCV kullanarak bir resim üzerinde yüz ve göz tespiti yapar:
#Yüz tespiti: `haarcascade_frontalface_default.xml` kullanılarak.
# Göz tespiti: `haarcascade_eye.xml` kullanılarak.
#Tespit edilen yüz ve gözler, resim üzerinde dikdörtgenlerle işaretlenir ve gösterilir.

import cv2
cascade_path=cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
eye_path=cv2.data.haarcascades + "haarcascade_eye.xml"

face_cascaded=cv2.CascadeClassifier(cascade_path)
eye_cascade=cv2.CascadeClassifier(eye_path)

img_path="human.jpg"

img=cv2.imread(img_path)

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces=face_cascaded.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))


for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)
    
    roi_gray =gray[y:y+h, x:x+w]
    roi_color=img[y:y+h, x:x+w]
    
    eyes=eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30) )
    
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,255),2)

    
    
    
cv2.imshow("win", img)
cv2.waitKey()
cv2.destroyAllWindows()
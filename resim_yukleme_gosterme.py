# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:02:53 2024

@author: usnis
"""
#Bu kod, OpenCV kullanarak bir resmi yükler, yeniden boyutlandırır ve iki resmi görüntüler. Ayrıca, bir resmi belirtilen yola kaydeder.

import cv2
img_path="araba.jpg"
img_path2="niss.jpg"
save_path= "araba_kopya.jpeg"
width=400
heigth=300


img= cv2.imread(img_path)
img2= cv2.imread(img_path2)


resized_image=cv2.resize(img, (width, heigth))


cv2.imshow("araba", resized_image)
cv2.imshow("niss", img2)

cv2.waitKey(0)  #kapatma komutu - 0 bir tuşa basınca kapat

cv2.destroyAllWindows()

cv2.imwrite(save_path, img)
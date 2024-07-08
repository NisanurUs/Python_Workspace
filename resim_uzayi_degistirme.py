# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:11:16 2024

@author: usnis
"""

#resim uzayını değişme
#Bu kod, bir resim dosyasını yükler ve bu resmi farklı renk uzaylarına (RGB, HSV, Gri) dönüştürür. Orijinal ve dönüştürülmüş resimleri görüntüler.

import cv2


img_path="araba.jpg"

img= cv2.imread(img_path)
rgb_img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
bgr=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray=cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)


cv2.imshow("orj", img)
cv2.imshow("rgb", rgb_img)
cv2.imshow("hsv", hsv_img)
cv2.imshow("gri",gray)




cv2.waitKey(0)
cv2.destroyAllWindows()
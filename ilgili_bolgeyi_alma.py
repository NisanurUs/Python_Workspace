# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:06:09 2024

@author: usnis
"""

#opencv ilgili bölgeyi alma 
#Bu kod, bir resim dosyasını yükler ve resim üzerinde belirli bir bölgeyi (ROI) seçer. Hem orijinal resmi hem de seçilen bölgeyi görüntüler.


import cv2

img=cv2.imread("araba.jpg")

roi=img[300:350, 450:550]  #ilgili bölgeyi alma "roi"

cv2.imshow("win", img)
cv2.imshow("roi", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:05:06 2024

@author: usnis
"""
#Bu kod, bir resmi yükler ve farklı blurlama (bulanıklaştırma) tekniklerini uygular:
# Median Blur: `cv2.medianBlur`
# Gaussian Blur: `cv2.GaussianBlur`
# Bilateral Filter: `cv2.bilateralFilter`
#Orijinal ve bulanıklaştırılmış resimleri görüntüler.

import cv2


img_path="araba.jpg"

img=cv2.imread(img_path)

median_blur= cv2.medianBlur(img, 15)  #blurlama işlemi için tek sayı olmalı 
gaussian_blur=cv2.GaussianBlur(img, (15,15), 0)
bileteral_blur=cv2.bilateralFilter(img, 15, 75, 95)


cv2.imshow("win", img)
cv2.imshow("med", median_blur)
cv2.imshow("gaus", gaussian_blur)
cv2.imshow("biletal", bileteral_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:42:51 2024

@author: usnis
"""

#Bu kod, rastgele üretilen iki veri kümesini kullanarak bir saçılım grafiği çizer:
# Rastgele verilerin oluşturulması: `np.random.rand` ile
# Saçılım grafiğinin çizilmesi: `plt.scatter`
# Grafik başlığı ve eksenlerin etiketlenmesi

import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(50)
y=np.random.rand(50)

plt.scatter(x, y)
plt.title("Saçılım")
plt.xlabel("x")
plt.ylabel("y")


plt.show


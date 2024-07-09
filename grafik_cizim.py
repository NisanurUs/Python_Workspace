# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:50:04 2024

@author: usnis
"""

import matplotlib.pyplot as plt
import numpy as np


x=["a","b","c","d"]
y=[13,62,73,34]

plt.bar(x, y)
plt.title("Bar Plot")
plt.xlabel("Sınıflar")
plt.ylabel("Değerler")

plt.show()

#%%

x="a","b","c","d"
y=[13,62,73,34]

plt.pie(y, labels=x, autopct="%1.1f%%")
plt.title("Pie Plot")
plt.xlabel("Sınıflar")
plt.ylabel("Değerler")

plt.show()

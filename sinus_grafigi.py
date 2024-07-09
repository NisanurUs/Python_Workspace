# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:47:42 2024

@author: usnis
"""

import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(0, 10, 100)
y=np.sin(x)

plt.plot(x, y)
plt.title("Sinüs")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
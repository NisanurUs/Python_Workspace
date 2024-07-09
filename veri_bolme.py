# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:32:47 2024

@author: usnis
"""

#Bu kod, rastgele boy ve kilo verilerini oluşturur ve bu verileri eğitim ve test setlerine böler:
# Verilerin oluşturulması: `np.random.normal` ile
# Eğitim ve test setlerine bölme: `train_test_split` fonksiyonu ile

import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split


np.random.seed(0)
boy=np.random.normal(170,10,30) # standart sapması 30 olan 10 değer üret
kilo=np.random.normal(70,10,30)


data=pd.DataFrame({"Boy" : boy, "kilo": kilo})

#%%

x= data["Boy"]
y=data["kilo"]

#%%

xtrain, xtest, ytrain, ytest=train_test_split(x,y,test_size=0.2, random_state=33)



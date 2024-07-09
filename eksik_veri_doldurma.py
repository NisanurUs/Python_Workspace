# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:21:55 2024

@author: usnis
"""

import pandas as pd
import numpy as np

data={"A": [1,2,np.nan,4,5],
      "B": [5,np.nan, np.nan,8,9],
      "C":[10,20,30,40,50]}


df=pd.DataFrame(data)

#%%

print("Veri seti: ", data)

#%%


#Eksik veriyi ortalama ile doldurma-inpute etme

#df["A"].fillna(df["A"].mean(), inplace=True)
#df["B"].fillna(df["B"].mean(), inplace=True)
#df["C"].fillna(df["C"].mean(), inplace=True)


#%%

#median ile doldurma

df["A"].fillna(df["A"].median(), inplace=True)
df["B"].fillna(df["B"].median(), inplace=True)
#%%

#mod ile doldurma

df["A"].fillna(df["A"].mode(), inplace=True)



#%%

#önceki değer ile doldurma

df["A"].fillna(method="ffill", inplace=True)

#bir sonraki değer ile 
df["B"].fillna(method="bfill", inplace=True)

#%%

#droplama eksik satırları

df_drop_rows=df.dropna()

#droplama eksik sütunları

df_drop_columns=df.dropna(axis=1)
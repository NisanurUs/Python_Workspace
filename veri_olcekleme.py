# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:51:42 2024

@author: usnis
"""
#Scikit learn ile normalizasyon


from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import numpy as np

data = np.array(([1.0, 2.0],
                [4.0, 5.0],
                [700.0, 800.0]))


standart_scaler= StandardScaler()
data_standart= standart_scaler.fit_transform(data)
print(data_standart)

#%%
scaler_minmax=MinMaxScaler()
data_minmax= scaler_minmax.fit_transform(data)
print(data_minmax)      
#%%
robut_scaler=RobustScaler()
data_robut=robut_scaler.fit_transform(data)
print(data_robut)


#%%


print("Standartlaştırılmış veri:\n " , data_standart)
print("Normalize edilmiş veri:\n " , data_minmax)
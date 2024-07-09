# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:44:03 2024

@author: usnis
"""

#Bu kod, kategorik verileri çeşitli tekniklerle kodlar:
# Label Encoding: `LabelEncoder`
# One-Hot Encoding: `OneHotEncoder`
# Pandas `get_dummies` fonksiyonu kullanılarak one-hot encoding
#Kategorik verilerin farklı şekillerde nasıl dönüştürüldüğünü gösterir.


from sklearn.preprocessing import LabelEncoder
import pandas as pd 

categories=["kırmızı", "mavi", "yeşil", "mavi", "kırmızı", "mor", "mavi","mavi"]

data=pd.DataFrame(categories)

#%%

#label encoder uyg
label_encoder=LabelEncoder()
data["encoded "]= label_encoder.fit_transform(data)

#%%

from sklearn.preprocessing import OneHotEncoder

categories=["kırmızı", "mavi", "yeşil", "mavi", "kırmızı", "mor", "mavi","mavi"]
data1=pd.DataFrame(categories, columns=["renkler"])

ohe=OneHotEncoder(sparse_output=False)


encoded_ohe=ohe.fit_transform(data1[["renkler"]])
column_names=ohe.get_feature_names_out(input_features=["renkler"])
encoded_df=pd.DataFrame(encoded_ohe,columns=column_names)

#%%

import pandas as pd

df2 = pd.DataFrame({"renkler": ["kırmızı", "mavi", "yeşil", "mavi", "kırmızı", "mor", "mavi", "mavi"]})

get_dummies = pd.get_dummies(df2, columns=["renkler"])



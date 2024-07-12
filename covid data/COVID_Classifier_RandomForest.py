# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:51:24 2024

@author: usnis
"""

import numpy as np
import pandas as pd
import PIL.Image as img
import os


from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# %%
covidli = "COVID"
covid_olmayan = "non-COVID"


def dosya(yol):
    return[os.path.join(yol, f) for f in os.listdir(yol)]


def veri_donustur(klasor_adi, sinif_adi):
    goruntuler = dosya(klasor_adi)
    goruntu_sinif = []

    for goruntu in goruntuler:
        goruntu_oku = img.open(goruntu).convert("L")
        goruntu_boyutu = goruntu_oku.resize((28, 28))
        goruntu_donusturme = np.array(goruntu_boyutu).flatten()

        if sinif_adi == "covidli":
            veriler = np.append(goruntu_donusturme, [0])

        elif sinif_adi == "covidli_olmayan":
            veriler = np.append(goruntu_donusturme, [1])

        else:
            continue
        goruntu_sinif.append(veriler)

    return goruntu_sinif
#%%
covidli_veri=veri_donustur(covidli, "covidli")
covidli_veri_df=pd.DataFrame(covidli_veri)


covidli_olmayan_veri=veri_donustur(covid_olmayan, "covidli_olmayan")
covidli_olmayan_veri_df=pd.DataFrame(covidli_olmayan_veri)

#%%

tum_veri=pd.concat([covidli_veri_df,covidli_olmayan_veri_df])

#%%

X = tum_veri.iloc[:, :-1].values  
y = tum_veri.iloc[:, -1].values   


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Randomm Forest
rf = RandomForestClassifier(n_estimators=50, random_state=23, max_depth=5)

# K-Fold çapraz doğrulama
kfold = KFold(n_splits=5, shuffle=True, random_state=43)
results = cross_val_score(rf, X_train, y_train, cv=kfold)

print(f"K-Fold CV Ortalama Doğruluk: {results.mean()}")

# Modeli eğitme
rf.fit(X_train, y_train)

# Test seti üzerinde tahmin yapma
y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Test Seti Doğruluğu: {accuracy}")

#%%
test="deneme/noncovid.png"
goruntu_oku1=img.open(test).convert("L")
goruntu_boyut1=goruntu_oku1.resize((28,28))
goruntu_donustur1=np.array(goruntu_boyut1).flatten()
goruntu_donustur2=goruntu_donustur1.reshape(1,-1)


result= rf.predict(goruntu_donustur2)
print(result)
if result[0]==0:
    print("seçilen resim covidli...")
elif result[0]==1:
    print("seçilen resim sağlıklı...")
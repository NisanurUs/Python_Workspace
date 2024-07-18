# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:00:16 2024

@author: usnis
"""

import numpy as np
# labirent matrisi
labirent =  np.array([
    [-100, -100, -100, -100, -100, 100, -100, -100, -100, -100],
    [-100, -1, -1, -1, -1, -1, -1, -1, -1, -100],
    [-100, -1, -100, -100, -100, -1, -100, -100, -1, -100],
    [-100, -1, -1, -1, -100, -1, -1, -1, -1, -1],
    [-100, -100, -100, -1, -100, -1, -100, -1, -100, -1],
    [-100, -1, -1, -1, -1, -1, -100, -1, -100, -100],
    [-100, -100, -100, -100, -1, -100, -100, -1, -1, -1],
    [-100, -100, -1, -1, -1, -1, -1, -1, -100, -1],
    [-100, -1, -100, -1, -100, -1, -100, -1, -1, -1],
    [-100, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100]
])
print("Labirent",labirent)

#%%

labirent_satir_sayisi, labirent_sutun_sayisi=labirent.shape
q_degerleri=np.zeros((labirent_satir_sayisi,labirent_sutun_sayisi,4))
hareketler=["SAG", "SOL", "YUKARI", "ASAGI"]
#%%
def engel_mi(gecerli_satir_index, gecerli_sutun_index):
    if labirent[gecerli_satir_index,gecerli_sutun_index]==-1:
        return False
    else:
        return True
#%%
def baslangic_belirle():
    gecerli_satir_index=np.random.randint(labirent_satir_sayisi)
    gecerli_sutun_index=np.random.randint(labirent_sutun_sayisi)
    while engel_mi(gecerli_satir_index, gecerli_sutun_index):
        gecerli_satir_index=np.random.randint(labirent_satir_sayisi)
        gecerli_sutun_index=np.random.randint(labirent_sutun_sayisi)
    
    return gecerli_satir_index,gecerli_sutun_index

#%%
def hareket_belirle(gecerli_satir_index,gecerli_sutun_index, epsilon):
    if np.random.random()<epsilon:
        return np.argmax(q_degerleri[gecerli_satir_index, gecerli_sutun_index])
    else:
       return np.random.randint(4)
        
#%%
def hareket_et(gecerli_satir_index,gecerli_sutun_index,hareket_index):
    yeni_satir_indeks=gecerli_satir_index
    yeni_sutun_index=gecerli_sutun_index
    
    if hareketler[hareket_index]=="SAG" and gecerli_sutun_index < labirent_sutun_sayisi -1:
        yeni_sutun_index+=1
    elif hareketler[hareket_index]=="SOL" and gecerli_sutun_index > 0:        
        yeni_sutun_index-=1
    elif hareketler[hareket_index]=="YUKARI" and gecerli_satir_index > 0:
        yeni_satir_indeks-=1
    elif hareketler[hareket_index]=="ASAGI" and gecerli_satir_index < labirent_satir_sayisi-1:
        yeni_satir_indeks+=1

    return yeni_satir_indeks,yeni_sutun_index

#%%

def en_kisa_yol(baslangic_satir_index, baslangic_sutun_index):
    if engel_mi(baslangic_satir_index,baslangic_sutun_index):
        return[]
    else:
        gecerli_satir_index,gecerli_sutun_index=baslangic_satir_index,baslangic_sutun_index
        en_kisa=[]
        en_kisa.append([gecerli_satir_index,gecerli_sutun_index])
        while not engel_mi(gecerli_satir_index, gecerli_sutun_index):
            hareket_index=hareket_belirle(gecerli_satir_index,gecerli_sutun_index,1)
            gecerli_satir_index,gecerli_sutun_index=hareket_et(gecerli_satir_index, gecerli_sutun_index, hareket_index)
            en_kisa.append([gecerli_satir_index,gecerli_sutun_index])
        return en_kisa
    
#%%

epsilon=0.9
azalma_degeri=0.9
ogrenme_orani=0.9
#%%

for adim in range(1000):
    satir_index,sutun_index=baslangic_belirle()
    while not engel_mi(satir_index, sutun_index):
        hareket_index=hareket_belirle(satir_index, sutun_index, epsilon)
        eski_satir_index, eski_sutun_index=satir_index,sutun_index
        satir_index,sutun_index=hareket_et(satir_index, sutun_index, hareket_index)
        odul=labirent[satir_index,sutun_index]
        eski_q_degeri=q_degerleri[eski_satir_index,eski_sutun_index,hareket_index]
        fark= odul + (azalma_degeri * np.max(q_degerleri[satir_index,sutun_index])) - eski_q_degeri
        yeni_q_degeri = eski_q_degeri + (ogrenme_orani + fark)
        q_degerleri[eski_satir_index,eski_sutun_index,hareket_index] = yeni_q_degeri


print("Eğitim tamamlandı...")
    
#%%
baslangic_satir, baslangic_sutun =input("Başlangıç konumunu girin :").split()
baslangic_satir=int(baslangic_satir)
baslangic_sutun=int(baslangic_sutun)
enkisarota=en_kisa_yol(int(baslangic_satir), int(baslangic_sutun))
if not enkisarota:
    print("Girdiğiniz koordinat geçersiz...")
else:
    print("Çıkışa giden yol")
    for i in range(len(enkisarota)-1):
        print(enkisarota[i])
   


#%%
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12,12))
ax.imshow(labirent, cmap='gray')
ax.set_xticks(range(labirent_sutun_sayisi))
ax.set_yticks(range(labirent_satir_sayisi))
ax.grid(color='k', linestyle='-', linewidth=1)
# Engelleri ve hedefi ekle
for satir in range(labirent_satir_sayisi):
    for sutun in range(labirent_sutun_sayisi):
        if labirent[satir, sutun] == -1:
            ax.add_artist(plt.Circle((sutun, satir), 0.3, color='r'))
        elif labirent[satir, sutun] == 100:
            ax.add_artist(plt.Circle((sutun, satir), 0.3, color='b'))
# Başlangıç noktasını ekle
ax.add_artist(plt.Circle((baslangic_sutun, baslangic_satir), 0.3, color='g'))
for i in range(len(enkisarota) - 1):
    ax.plot([enkisarota[i][1], enkisarota[i+1][1]],
            [enkisarota[i][0], enkisarota[i+1][0]], color='b', linewidth=6)
plt.show()     
    
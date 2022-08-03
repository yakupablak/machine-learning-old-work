# -*- coding: utf-8 -*-
"""
Created on Sun May 15 16:41:03 2022

@author: yakup
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data=pd.read_csv("eksikveriler.csv")
 #eksik olan nan degerler yerine ortalama degerler verilecek
 
from sklearn.impute import SimpleImputer
imputer =SimpleImputer(missing_values=np.nan, strategy="mean")
age=data.iloc[:,1:4].values#1. 2. ve 3. kolonuçektik
print(age)
imputer =imputer.fit(age[:,1:4])#mean stratejisi ile öğrenme gerçekleştiriliyor
age[:,1:4]= imputer.transform(age[:,1:4])#doldurulmus bosluklar age verisine tamamlanıyor
                                  
country= data.iloc[:,0:1].values#ülkenin olduğu kolonu yani 0. kolonu çekiyoruz
print(country)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()#ülkeleri sayısal degere convert edecek encoder call ediliyor
country[:,0]=le.fit_transform(data.iloc[:,0])
print(country)
ohe =preprocessing.OneHotEncoder()# sayısal veriyi 1 ve 0 a convert edecek method call ediliyor
country=ohe.fit_transform(country).toarray()# 1 ve 0 lı arraye convert edioruz
print(country)
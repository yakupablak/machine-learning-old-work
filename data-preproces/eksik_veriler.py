# -*- coding: utf-8 -*-
"""
Created on Sun May 15 16:41:03 2022

@author: yakup
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data=pd.read_csv("eksikveriler.csv")
 #eksik lan nan degerler yerine ortalama degerler verilecek
 
from sklearn.impute import SimpleImputer
imputer =SimpleImputer(missing_values=np.nan, strategy="mean")
age=data.iloc[:,1:4].values#1. 2. ve 3. kolonuçektik
print(age)
imputer =imputer.fit(age[:,1:4])#mean stratejisi ile öğrenme gerçekleştiriliyor
age[:,1:4]= imputer.transform(age[:,1:4])#doldurulmus bosluklar age verisine tamamlanıyor
                                  
print(age)
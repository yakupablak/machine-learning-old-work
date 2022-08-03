# -*- coding: utf-8 -*-
"""
Created on Sun May 15 16:41:03 2022

@author: yakup
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#1.veri on isleme
#1.1 veri yukleme
data=pd.read_csv("eksikveriler.csv")

#encoder nominal ordinal>numeric                                  
country= data.iloc[:,0:1].values#ülkenin olduğu kolonu yani 0. kolonu çekiyoruz
print(country)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()#ülkeleri sayısal degere convert edecek encoder call ediliyor
country[:,0]=le.fit_transform(data.iloc[:,0])
print(country)
ohe =preprocessing.OneHotEncoder()# sayısal veriyi 1 ve 0 a convert edecek method call ediliyor
country=ohe.fit_transform(country).toarray()# 1 ve 0 lı arraye convert edioruz

result1 = pd.DataFrame(data=country,index=range(22),columns=["fr","tr","us"])#0 dan 21 e sırlayıp veri baslıklarını fr tr ve us olarak ayırıyoruz
print(result1)
result2 =pd.DataFrame(data=age,index=range(22),columns=["boy","kilo","yas"])
print(result2)
gender=data.iloc[:,-1].values#data frame deki son kolonu yani cinsiyeti çekme
print(gender)
result3= pd.DataFrame(data=gender,index=range(22),columns=["gender"])
print(result3)
s=pd.concat([result1,result2],axis=1)#yan yana birlestirme icin axis e 1 dedik
print(s)
finalResult=pd.concat([s,result3],axis=1)

######################################




from sklearn.model_selection import train_test_split
#%33 test olacak sekilde cinsiyeti tespit etmek icin train ve test olarak veriler ayrılacak
train_x, test_x, train_y, test_y=train_test_split(s,result3,test_size=0.33, random_state=0) 

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
train_x_scaled=sc.fit_transform(train_x)# birbirine daha yakın değerler olarak scale ediliyor







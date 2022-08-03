# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:50:13 2020

@author: sadievrenseker
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
data = pd.read_csv('satislar.csv')
#pd.read_csv("veriler.csv")
#test
print(data)

month=data[["Aylar"]]
print(month)

sales=data[["Satislar"]]
print(sales)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(month,sales,test_size=0.33, random_state=0)
"""
#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#MODEL İNSASİ
from sklearn.linear_model import  LinearRegression #dogrysal model olusturmak icin cagirdik
lr= LinearRegression()
lr.fit(X_train, Y_train)


prediction=lr.predict(X_test)



"""

#MODEL İNSASİ
from sklearn.linear_model import  LinearRegression #dogrysal model olusturmak icin cagirdik
lr= LinearRegression()
lr.fit(x_train, y_train)


prediction=lr.predict(x_test)
x_train=x_train.sort_index()
y_train=y_train.sort_index()
plt.plot(x_train,y_train)
#tahmini yazdiricaz
plt.plot(x_test,lr.predict(x_test))






























"""
x = veriler.iloc[:,1:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken
print(y)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)


from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)

"""
















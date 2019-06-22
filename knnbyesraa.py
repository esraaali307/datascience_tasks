# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:53:08 2019

@author: A
"""

import csv
import numby as np 
import pandas as pd
#from pandas import DataFrame
from sklearn import neighbors, datasets

import math
import itertools


df = pd.read_csv('training.csv',sep=';')
#print(df.head())
df = pd.read_csv('validation.csv',sep=';')
#print(df.head())
def loadData(fileName):
    df = pd.read_csv(fileName,sep=',',header=None)
    X = df[df.columns[0:19]]
    y = df[19]
    return X.values , y.values

def eculidenDistance(x , xi):
    d = 0.0
    for i in range(len(x)):
        d += pow(abs(x[i]-xi[i]),2)
    return math.sqrt(d)

def getKey(item):
    return item[1]

def knnPredictor(train,test,k):
     X = train[0]
     y = train[1]
     Xt = test[0]
     yt = test[1]
    
     cnt = 0 
    for i in range(len(Xt)):
        newDataSet = []
        for j in range(len(X)):
            newDataSet.append([j,eculidenDistance(X[j],Xt[i]),y[j]])
            
            newDataSet = sorted(newDataSet,key=getKey)
        dict = {} #for maximum label
        keyOfMaxItem = ''
        for item in itertools.islice(newDataSet , 0, k):
            key = item[2]
            keyOfMaxItem = key
            if key in dict:
                dict[key] = dict[key] + 1 
            else:
                dict[key] = 1
                 for key in dict:
            if dict[key] >= dict[keyOfMaxItem]:
                keyOfMaxItem = key
        if keyOfMaxItem == yt[i]:
            cnt += 1
             accuracy = (float(cnt)/len(Xt))*100
              print("Accuracy = ",accuracy)
    X , y = loadData('training.xlsx')
Xt , yt = loadData('validation.xlsx')
print(len(y))

for k in range(3,9+1):
    n_neighbors = k
    print("K = ",k)
    knnPredictor([X,y],[Xt,yt],n_neighbors)
    

            
            
            
            
            
    
    
    
    
    
    
    


    
    

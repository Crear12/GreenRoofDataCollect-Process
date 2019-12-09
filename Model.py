#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:28:35 2019

@author: Crear
"""
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def linear(x,y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    
    xfit = np.linspace(0, 500, 10000)
    yfit = model.predict(xfit[:, np.newaxis])
    
    plt.scatter(x, y)
    plt.plot(xfit, yfit)

if __name__ == '__main__':
    MT = pd.read_csv('Mois_Temp_Nov28-Dec1.csv')
    y_Mois = MT['Relative Mois']
    y_Temp = MT['Temperature(C)']
    x = MT['Time(s)']
    deriMoi = []
    deltaT = []
    for i in range(np.shape(y_Mois)[0]-1):
        deriMoi.append((y_Mois[i+1]-y_Mois[i])/10)
        deltaT.append(y_Temp[i]-np.mean(y_Temp))
#    plt.plot(x[1:],np.asarray(deriMoi))
#    plt.plot(x[1:],np.asarray(deltaT))
#    plt.plot(-np.asarray(deltaT),np.asarray(deriMoi))
    linear(-np.asarray(deltaT),np.asarray(deriMoi))
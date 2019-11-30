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
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
def linear(x,y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    
    xfit = np.linspace(0, 500, 10000)
    yfit = model.predict(xfit[:, np.newaxis])
    
    plt.scatter(x, y)
    plt.plot(xfit, yfit)

def poly(x,y):
    poly_model = make_pipeline(PolynomialFeatures(30),
                           LinearRegression())
    poly_model.fit(x[:, np.newaxis], y)
    xfit = np.linspace(0, 500, 10000)
    yfit = poly_model.predict(xfit[:, np.newaxis])
    plt.scatter(x, y)
    plt.plot(xfit, yfit)

from sklearn.base import BaseEstimator, TransformerMixin

class GaussianFeatures(BaseEstimator, TransformerMixin):
    """Uniformly spaced Gaussian features for one-dimensional input"""
    
    def __init__(self, N, width_factor=2.0):
        self.N = N
        self.width_factor = width_factor
    
    @staticmethod
    def _gauss_basis(x, y, width, axis=None):
        arg = (x - y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))
        
    def fit(self, X, y=None):
        # create N centers spread along the data range
        self.centers_ = np.linspace(X.min(), X.max(), self.N)
        self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        return self
        
    def transform(self, X):
        return self._gauss_basis(X[:, :, np.newaxis], self.centers_,
                                 self.width_, axis=1)
def gauss(x,y):   
    gauss_model = make_pipeline(GaussianFeatures(20),
                                LinearRegression())
    gauss_model.fit(x[:, np.newaxis], y)
    xfit = np.linspace(0, 500, 10000)
    yfit = gauss_model.predict(xfit[:, np.newaxis])
    plt.scatter(x, y)
    plt.plot(xfit, yfit)
    plt.xlim(0, 10)

if __name__ == '__main__':
    MT = pd.read_csv('Mois_Temp.csv')
    y_Mois = MT['Relative Mois']
    y_Temp = MT['Temperature(C)']
    x = MT['Time(s)']
#    linear(x,y_Mois)
#    linear(x,y_Temp)
#    poly(x,y_Mois)
#    poly(x,y_Temp)
    gauss(x,y_Mois)
    gauss(x,y_Temp)
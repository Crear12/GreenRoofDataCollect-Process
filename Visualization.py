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


if __name__ == '__main__':
    MT = pd.read_csv('Mois_Temp.csv')
    y_Mois = MT['Relative Mois']
    y_Temp = MT['Temperature(C)']
    x = MT['Time(s)']
    MT.plot.scatter(x='Time(s)', y='Relative Mois')
    MT.plot.scatter(x='Time(s)', y='Temperature(C)')
    MT.plot.hexbin(x='Time(s)', y='Relative Mois', gridsize=15)
    MT.plot.hexbin(x='Time(s)', y='Temperature(C)', gridsize=15)
    MT.plot.hist(x='Time(s)', y='Relative Mois')
    MT.plot.hist(x='Time(s)', y='Temperature(C)')
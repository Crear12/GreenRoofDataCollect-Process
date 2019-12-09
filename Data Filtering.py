#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:28:35 2019

@author: Crear
"""
import numpy as np
import pandas as pd
from pandas.plotting import autocorrelation_plot, lag_plot
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.fftpack import rfft, irfft, fftfreq

def plt_autoCorr(originalSignal,typeofdata):
    fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(8,3))
    
    timeLags = np.arange(1,500)
    autoCorr = [originalSignal.autocorr(lag=dt) for dt in timeLags]
    ax.plot(timeLags, autoCorr);
    ax.set_xlabel('time lag [10 seconds]'); ax.set_ylabel('correlation coeff'+typeofdata, fontsize=12);

def filt(originalSignal,windowSize):
    lowPassFilteredSignal = originalSignal.rolling(windowSize, center=True).mean()
    highPassFilterdSignal = originalSignal - lowPassFilteredSignal
    return lowPassFilteredSignal, highPassFilterdSignal

def mov_average(originalSignal, passedSignal, typeofdata, passtype):    
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(8,3))
    ax.plot(t0,originalSignal,c='y')
    ax.plot(t0,passedSignal,c='r')
    ax.legend(['original signal',passtype+' pass filtered'], fontsize=18,
                  loc='upper left',bbox_to_anchor=(0.02,1.4), ncol=1)
    ax.set_ylabel(typeofdata, fontsize=11)

def FFT(signal):
    W = fftfreq(signal.size, d=10)
    f_signal = rfft(signal)
    plt.figure(1)
    plt.plot(W,f_signal)
    
#    # If our original signal time was in seconds, this is now in Hz    
#    cut_f_signal = f_signal.copy()
#    cut_f_signal[(W<6)] = 0
#    
#    cut_signal = irfft(cut_f_signal)
##    print(cut_signal)
#    plt.figure(2)
#    plt.plot(cut_signal)
    
if __name__ == '__main__':
    MT = pd.read_csv('Mois_Temp.csv')
    t0 = MT.index
    lowMois, highMois = filt(MT['Relative Mois'],2)
    lowTemp, highTemp = filt(MT['Temperature(C)'],2)
    print(lowMois,highMois,lowTemp, highTemp)
    FFT(lowMois)
    FFT(highMois)
    FFT(lowTemp)
    FFT(highTemp)
    
    mov_average(MT['Relative Mois'],lowMois,'Relative Mois','low')
    mov_average(MT['Relative Mois'],highMois,'Relative Mois','high')
    mov_average(MT['Temperature(C)'],lowTemp,'Temperature [$^\circ$C]','low')
    mov_average(MT['Temperature(C)'],highTemp,'Temperature [$^\circ$C]','high')
    
    plt_autoCorr(lowMois,'Relative Mois')
    plt_autoCorr(highMois,'Relative Mois')
    plt_autoCorr(lowTemp,'Temperature')
    plt_autoCorr(highTemp,'Temperature')
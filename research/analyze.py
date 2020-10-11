# import current directry python files
import fitting as ft
import plot as pl
import baseline_correction as bs
# import python library
import numpy as np
import scipy.optimize
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import os
import pandas as pd
import csv

#save_dir = '../../研究/M1/週報/9月/' #Lab
save_dir = '../../../../奈良先端大研究/M1/週報/10月' #PC

#initial value
HWHM = 1.5
n_air = 1.002
n_water = 1.3330
n_ph3 = 1.448
h = 6.62607*10.0**-34
e = 1.6*10.0**-19
c = 2.9972*10**8
Lc = 6.71*10**-4
E0 = 2100.0 # cavity mode
Ev = 2115.0461 # sample absorption

def Lorentz_fit(x1,y1):
    max_y = max(y1)
    min_y = min(y1)
    if np.abs(max_y) >= np.abs(min_y):
        intensity = max_y
        x_peak = x1[np.argmax(y1)]

    else:
        intensity = min_y
        x_peak = x1[np.argmin(y1)]
    
    # 初期値の設定
    pini = np.array([intensity, x_peak, 1])
    # フィッティング
    ft.Lorentz_func(x1, intensity, x_peak, HWHM)

    popt, pcov = scipy.optimize.curve_fit(ft.Lorentz_func, x1, y1, p0=pini)
    perr = np.sqrt(np.diag(pcov))

    # datファイルへのフィッティング結果の書き込み
    #result.writelines(name + '\t' + '\t'.join([str(p) + '\t' + str(e)  for p, e in zip(popt, perr)]) + '\n')

    # フィッティング曲線描画用の配列を作成
    fitline = ft.Lorentz_func(x1, popt[0], popt[1], popt[2])
    plot(x1,y1,fitline,y1)
    print(popt[1])
    return popt[1]

def fsr(x1,y1):
    a, _ = find_peaks(y1, height=12, distance=90)
    # fsr value
    fsr_value = x1[a[1]]-x1[a[0]]
    print('FSR = ',fsr_value)
    print(x1[a[0]],x1[a[1]])
    # Real cavity length [um]
    l = 1/(2*n_water*fsr_value*10**-4)
    print('Real cavity length (vacant) :',l)
    plot(x1,y1,x1[a],y1[a])

def rabi_splitting(x1,y1,i):
    a, _ = find_peaks(y1, height=0.1, distance=90)
    if i == 0:
        x_U = x1[a[1]]
        #x_L = x1[a[0]-20:a[0]+120]
        #y_L = y1[a[0]-20:a[0]+120]
        #x_U = x1[a[1]-15:a[1]+60]
        #y_U = y1[a[1]-15:a[1]+60]
        #x_L = Lorentz_fit(x_L,y_L)
        #x_U = Lorentz_fit(x_U,y_U)
        a, _ = find_peaks(y1, height=0.58, distance=10)
        x_L = x1[a[1]]
        return x_L,x_U
    else :
        x_L = x1[a[0]]
        x_U = x1[a[1]]
        return x_L,x_U


def reflective_index():
    l = input('Real cavity length [um] : ')
    fsr_solution = input('fsr(solution) [1/cm] : ')
    return 1.0/(2.0*float(l)*float(fsr_solution)*10.0**-4.0)

def polariton():
    y = []
    y_ini = []
    popt_ini = []
    theta = []
    file = os.path.abspath('result/100nmSiO2_6um_pola.csv')
    f = pd.read_csv(file,encoding='utf-8',names=('A', 'B', 'C'))
    X = f['A']
    Y1 = f['B']
    Y2 = f['C']
    x = np.array(X)
    y1 = np.array(Y1)
    y2 = np.array(Y2)
    y3 = y2-y1
    '''
    y.append(y1)
    y.append(y2)
    y_ini.append(y1[0])
    y_ini.append(y2[0])
    '''
    pini = np.array(y3[0])
    popt1, pcov = scipy.optimize.curve_fit(ft.Lpolariton_fit, x, y1, p0=pini)
    popt2, pcov = scipy.optimize.curve_fit(ft.Upolariton_fit, x, y2, p0=pini)
    Rabi1 = ft.Lpolariton_fit(x,popt1)
    Rabi2 = ft.Upolariton_fit(x,popt2)
    El = ft.cavity_mode(x)


    
    #plot
    #fig = plt.figure()
    plt.plot(x,Rabi1)
    plt.plot(x,Rabi2)
    plt.plot(x,El)
    plt.scatter(x,y1)
    plt.scatter(x,y2)
    plt.axhline(y = Ev, xmin=0,xmax=20)
    plt.title('Potassium Hexacyanoferrate(3)',fontsize=16)
    plt.xlabel('Angle [deg]',fontsize=16) 
    plt.ylabel('Wave number [cm-1]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.2)
    plt.show()
    #fig.savefig(os.path.join(save_dir, 'not_coated_cavity_polariton_6um.png'))

    return y2[4]-y1[4]




def plot(x,fix1,fix2,fix3):
    input_data = input('plot type: t = transmittance, a = absorbance, s = singlebeam : ')
    
    if input_data == 'a':
        pl.Abs(x,fix1,fix2,fix3)
    if input_data == 't':
        pl.Trans(x,fix1,fix2,fix3)
    if input_data == 's':
        pl.Single(x,fix1,fix2,fix3)
    else :
        print("input a or t or s")
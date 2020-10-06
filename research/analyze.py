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
HWHM = 1
n_air = 1.002
n_water = 1.3330
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

def fsr(x1,y1):
    a, _ = find_peaks(y1, height=0.2, distance=40)
    # fsr value
    fsr_value = x1[a[-1]]-x1[a[-2]]
    print('FSR = ',fsr_value)
    print(x1[a[0]],x1[a[1]])
    # Real cavity length [um]
    #l = 1/(2*n_ph3*fsr_value*10**-4)
    #print('Real cavity length (vacant) :',l)
    plot(x1,y1,x1[a],y1[a])



def reflective_index():
    l = input('Real cavity length [um] : ')
    fsr_solution = input('fsr(solution) [1/cm] : ')
    return 1.0/(2.0*float(l)*float(fsr_solution)*10.0**-4.0)

def polariton():
    theta = np.arange(0,22,2)
    file = os.path.abspath('../../../../奈良先端大研究/yamada/20200915/polariton.csv')
    f = pd.read_csv(file,encoding='utf-8',names=('A', 'B', 'C'))
    X = f['A']
    Y1 = f['B']
    Y2 = f['C']
    x = np.array(X)
    y1 = np.array(Y1)
    y2 = np.array(Y2)
    y3 = y2-y1
    pini = np.array([E0])
    popt1, pcov = scipy.optimize.curve_fit(ft.Lpolariton_fit, x, y1, p0=pini)
    popt2, pcov = scipy.optimize.curve_fit(ft.Upolariton_fit, x, y2, p0=pini)
    fitline1 = ft.Lpolariton_fit(x,popt1[0])
    fitline2 = ft.Upolariton_fit(x,popt2[0])
    print(popt1[0])
    print(popt2[0])
    L_cavity = ft.cavity_mode(theta,popt1[0])
    U_cavity = ft.cavity_mode(theta,popt2[0])
    
    #plot
    #fig = plt.figure()
    plt.plot(theta,fitline1)
    plt.plot(theta,fitline2)
    plt.plot(theta,L_cavity)
    plt.plot(theta,U_cavity)
    plt.scatter(x,y1)
    plt.scatter(x,y2)
    plt.axhline(y = Ev, xmin=0,xmax=20)
    plt.title('Potassium Hexacyanoferrate(3)',fontsize=16)
    plt.xlabel('Angle [deg]',fontsize=16) 
    plt.ylabel('Wave number [cm-1]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.2)
    plt.legend()
    plt.show()
    #fig.savefig(os.path.join(save_dir, 'not_coated_cavity_polariton_6um.png'))




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
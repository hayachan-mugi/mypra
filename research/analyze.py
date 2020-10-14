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

save_dir = '../../研究/M1/週報/10月/' #Lab
#save_dir = '../../../../奈良先端大研究/M1/週報/10月' #PC

#initial value
HWHM = 1.5
n_air = 1.002
n_water = 1.3330
n_ph3 = 1.57
h = 6.62607*10.0**-34
e = 1.6*10.0**-19
c = 2.9972*10**8
Lc = 6.71*10**-4
E0 = 2108.0 # cavity mode
Em = 2115.0 # sample absorption

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
    a, _ = find_peaks(y1, height=0.3, distance=50)
    # fsr value
    #b = x1[max(y1)]
    #print(b)
    fsr_value = x1[a[1]]-x1[a[0]]
    print('FSR = ',fsr_value)
    print(x1[a[0]],x1[a[1]])
    # Real cavity length [um]
    l = 1/(2*n_water*fsr_value*10**-4)
    print('Real cavity length (vacant) :',l)
    plot(x1,y1,x1[a],y1[a])

def rabi_splitting(x1,y1,i):
    a, _ = find_peaks(y1, height=0.19, distance=90)
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
    file = os.path.abspath('result/notcoated_6um_pola.csv')
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
    y = y1+y2
    y.reshape(1,len(y))

    pini = np.array([y3[0],n_ph3,E0,Em]) #Parameter Rabispitting,matter Spectra() 
    popt1, pcov = scipy.optimize.curve_fit(ft.polariton_fit, x, y, p0=pini, bounds=([40.,1.3,2090.,2090.],[80.,1.8,2120.,2120.]))
    #popt2, pcov = scipy.optimize.curve_fit(ft.Upolariton_fit, x, y2, p0=pini)
    x1 = np.arange(-30, 31, 1)
    Rabi_L = ft.Lpolariton_fit(x1,popt1[0],popt1[1],popt1[2],popt1[3])
    Rabi_U = ft.Upolariton_fit(x1,popt1[0],popt1[1],popt1[2],popt1[3])
    El = ft.cavity_mode(x1,n_ph3,popt1[2])
    #print(pcov[0],pcov[1],pcov[2],pcov[3])
    perr = np.sqrt(np.diag(pcov[1]))
    print(perr)
    print(popt1[0],popt1[1],popt1[2],popt1[3])


    
    #plot
    fig = plt.figure()
    plt.plot(x1,Rabi_L, label='LP')
    plt.plot(x1,Rabi_U, label='UP')
    plt.plot(x1,El, label='Cavity mode')
    plt.scatter(x,y1)
    plt.scatter(x,y2)
    plt.axhline(y = popt1[3], xmin=0,xmax=20, label='Absorption spectra')
    plt.title('Potassium Hexacyanoferrate(3)',fontsize=19)
    plt.xlabel('Angle [deg]',fontsize=19) 
    plt.ylabel('Wave number [cm-1]',fontsize=19)
    plt.text(0.8, 80, '57.85400000000027 1.577594526556183 2105.165651139043 2111.0643234273452', va='bottom')
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.2)
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=10)
    plt.show()
    fig.savefig(os.path.join(save_dir, 'not_coated_cavity_polariton_6um.png'))

    return y2[3]-y1[3]




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
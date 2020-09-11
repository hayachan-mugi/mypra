import fitting as ft
import plot as pl
import numpy as np
import scipy.optimize
import glob, re
from functools import cmp_to_key
from scipy.signal import find_peaks

HWHM = 5

def Lorentz_func(x, intensity, X0, HWHM):
    return intensity * HWHM**2 / ((x-X0)**2 + HWHM**2)

def fit(x1,y1):
    max_y = max(y1)
    min_y = min(y1)
    print("a")
    if np.abs(max_y) >= np.abs(min_y):
        intensity = max_y
        x_peak = x1[np.argmax(y1)]

    else:
        intensity = min_y
        x_peak = x1[np.argmin(y1)]
    print(x_peak)
    # 初期値の設定
    pini = np.array([intensity, x_peak, 1])
    print(pini)
    # フィッティング
    Lorentz_func(x1, intensity, x_peak, HWHM)

    popt, pcov = scipy.optimize.curve_fit(Lorentz_func, x1, y1, p0=pini)
    perr = np.sqrt(np.diag(pcov))

    # 結果の表示
    print("initial parameter\toptimized parameter")
    for i, v  in enumerate(pini):
        print(str(v)+ '\t' + str(popt[i]) + ' ± ' + str(perr[i]))

    # datファイルへのフィッティング結果の書き込み
    #result.writelines(name + '\t' + '\t'.join([str(p) + '\t' + str(e)  for p, e in zip(popt, perr)]) + '\n')

    # フィッティング曲線描画用の配列を作成
    fitline = Lorentz_func(x1, popt[0], popt[1], popt[2])
    plot(x1,fitline,y1,y1)



def fsr(x1,y1):
    a, _ = find_peaks(y1, height=43, distance=100)
    print(a)
    print(_)
    print(x1[a])# fsr value
    e = x1[a[-1]]-x1[a[-2]]
    print(e)
    plot(x1,y1,x1[a],y1[a])


    

#def reflective_index(x1,y1):


def plot(x,fix1,fix2,fix3):
    input_data = input('plottype: t = transmittance, a = absorbance, s = singlebeam = ')
    
    if input_data == 'a':
        pl.Abs(x,fix1,fix2,fix3)
    if input_data == 't':
        pl.Trans(x,fix1,fix2,fix3)
    if input_data == 's':
        pl.Single(x,fix1,fix2,fix3)
    else :
        print("input a or t or s")
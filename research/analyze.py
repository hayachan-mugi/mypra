# import current directry python files
import fitting as ft
import plot as pl
import baseline_correction as bs
# import python library
import numpy as np
import scipy.optimize
from scipy.signal import find_peaks

HWHM = 1
n_air = 1.002
n_water = 1.3330

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
    a, _ = find_peaks(y1, height=15, distance=270)
    # fsr value
    fsr_value = x1[a[-2]]-x1[a[-3]]
    print(fsr_value)
    # Real cavity length [um]
    l = 1/(2*n_air*fsr_value*10**-4)
    print('Real cavity length (vacant) :',l)
    plot(x1,y1,x1[a],y1[a])



def reflective_index():
    l = input('Real cavity length [um] : ')
    fsr_solution = input('fsr(solution) [1/cm] : ')
    return 1.0/(2.0*float(l)*float(fsr_solution)*10.0**-4.0)



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
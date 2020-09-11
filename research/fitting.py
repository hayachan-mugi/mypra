import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import plot as pl

def gauss_func(x, a, mu, sigma):

    return a*np.exp(-(x-mu)**2/(2*sigma**2))

def Lorentz_func(x, intensity, X0, HWHM):
    return intensity * HWHM**2 / ((x-X0)**2 + HWHM**2)

def P_fit(x,y):
    z = np.polyfit(x,y,7)
    print(z)
    fix = np.poly1d(z)
    fix = fix(x)
    #preplot()
'''   
def preplot():
    input_data = input('plottype: t = transmittance, a = absorbance, s = singlebeam = ')

    if input_data == 'a':
        pl.Abs(x,y,x,fix)
    if input_data == 't':
        pl.Trans(x,y,x,fix)
    if input_data == 's':
        pl.Single(x,y,x,fix)
    else :
        print("input a or t or s")
'''
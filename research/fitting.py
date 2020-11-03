import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import plot as pl

#E0 = 2108.5 #透過率の等しいデータを採用
 #absorption spectra
n_ph3 = 1.381 #Reflective index
e = 1.6*10.0**-19
Lc = 7.053*10**-6
c = 2.9972*10**8
h = 6.62607*10.0**-34
eV = h*c*100/e
m = 4.0 #mode
Em = 2115.0*eV

def gauss_func(x, a, mu, sigma):

    return a*np.exp(-(x-mu)**2/(2*sigma**2))

def Lorentz_func(x, intensity, X0, HWHM):
    return intensity * HWHM**2 / ((x-X0)**2 + HWHM**2)

def Poly_fit(x,y):
    z = np.polyfit(x,y,7)
    print(z)
    fix = np.poly1d(z)
    fix = fix(x)
    return fix

def polariton_fit(theta,q,Lc):

    P=[]
    q = q*eV
    E2 = cavity_mode(theta,Lc)
    P1 = (Em+E2)/2 - (((q)**2 + (Em-E2)**2)**(1/2))/2
    P2 = (Em+E2)/2 + (((q)**2 + (Em-E2)**2)**(1/2))/2
    P = np.append(P,P1)
    P = np.append(P,P2)
    P = P/eV
    
    return P


def cavity_mode(theta,Lc):

    E0 = (m*h*c)/(2*n_ph3*Lc*e)
    E = E0*((1-(((1-np.cos(np.radians(2*theta)))/2)/(n_ph3**2)))**(-1/2))
    return E


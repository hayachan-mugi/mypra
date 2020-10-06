import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import plot as pl

E1 = 2115.0461 #absorption spectra
n_ph3 = 1.448 #Reflective index


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

def Lpolariton_fit(theta,E0):
    E2 = cavity_mode(theta,E0)
    sigma_L = (E1+E2)/2 - ((q)**2 + (E1-E2)**2)**(1/2)
    return sigma_L

def Upolariton_fit(theta,E0):
    E2 = cavity_mode(theta,E0)
    sigma_U = (E1+E2)/2 + ((q)**2 + (E1-E2)**2)**(1/2)
    return sigma_U

def cavity_mode(theta,E0):
    return E0*((1-((1-np.cos(np.radians(2*theta)))/2)/n_ph3**2)**(-1/2))

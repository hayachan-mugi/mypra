import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csc_matrix
from scipy.sparse import spdiags
import scipy.sparse.linalg as spla
import os
import pandas as pd
import plot as pl

#パラメタを入力します、うまく推定ができないときはここをいじってください
#AsLSでのベースライン推定は ( W(p) + lam*D'D )z = Wy のとき、重み p と罰則項の係数 lam がパラメタです
# paramAsLS = [ lam1 , p ]

paramAsLS = [10**3.5, 0.00005]

#AsLSによりベースライン推定を行います
def baseline_als(y, lam, p, niter=10):
    #https://stackoverflow.com/questions/29156532/python-baseline-correction-library
    #p: 0.001 - 0.1, lam: 10^2 - 10^9
    # Baseline correction with asymmetric least squares smoothing, P. Eilers, 2005
    L = len(y)
    D = csc_matrix(np.diff(np.eye(L), 2))
    w = np.ones(L)
    for i in range(niter):
        W = spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spla.spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z


#csvファイルと図を出力します
def outFigCSV(x,y):

    # baseline estimation and smoothing
    Y_np = np.array(y)
    bkg = baseline_als(Y_np,paramAsLS[0], paramAsLS[1])
    fix = Y_np - bkg

    input_data = input('plottype: t = transmittance, a = absorbance, s = singlebeam = ')
    
    if input_data == 'a':
        pl.Abs(x,y,bkg,fix)
    if input_data == 't':
        pl.Trans(x,y)
    if input_data == 's':
        pl.Single(x,y)
    else :
        print("input a or t or s")

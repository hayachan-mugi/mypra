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
def outFigCSV(x,y1,y2,y3):

    # baseline estimation
    Y_np1 = np.array(y1)
    bkg1 = baseline_als(Y_np1,paramAsLS[0], paramAsLS[1])
    fix1 = Y_np1 - bkg1
    Y_np2 = np.array(y2)
    bkg2 = baseline_als(Y_np2,paramAsLS[0], paramAsLS[1])
    fix2 = Y_np2 - bkg2
    Y_np3 = np.array(y3)
    bkg3 = baseline_als(Y_np3,paramAsLS[0], paramAsLS[1])
    fix3 = Y_np3 - bkg3

    input_data = input('plottype: t = transmittance, a = absorbance, s = singlebeam = ')
    
    if input_data == 'a':
        pl.Abs(x,fix1,fix2,fix3)
    if input_data == 't':
        pl.Trans(x,fix1,fix2,fix3)
    if input_data == 's':
        pl.Single(x,fix1,fix2,fix3)
    else :
        print("input a or t or s")

# import current directry python files
import plot as pl
# import python library
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse import spdiags
import scipy.sparse.linalg as spla

#パラメタを入力します、うまく推定ができないときはここをいじってください
#AsLSでのベースライン推定は ( W(p) + lam*D'D )z = Wy のとき、重み p と罰則項の係数 lam がパラメタです
# paramAsLS = [ lam1 , p ] defult value
#0.001 ≤ p ≤ 0.1 is a good choice (for a signal with positive peaks) and 10^2 ≤ λ ≤ 10^9

#paramAsLS = [10**3.5, 0.00005]
paramAsLS = [10**5.5, 0.00005]
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
def baseline(x,y1,y2,y3):

    # baseline estimation
    bkg1 = baseline_als(y1,paramAsLS[0], paramAsLS[1])
    fix1 = y1 - bkg1
    bkg2 = baseline_als(y2,paramAsLS[0], paramAsLS[1])
    fix2 = y2 - bkg2
    bkg3 = baseline_als(y3,paramAsLS[0], paramAsLS[1])
    fix3 = y3 - bkg3

    input_data = input('if you input the [c] , you can check baseline correction. other = return the value : ')
    
    if input_data == 'c':
        pl.Check(x,y3,fix3,bkg3)
    else :
        return x,fix1,fix2,fix3
    
    return x,fix1,fix2,fix3

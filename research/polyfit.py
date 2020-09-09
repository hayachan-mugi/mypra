import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def data_change(file):
    f = pd.read_csv(file)
    #f.columns=list('XY')
    '''
    d1 = f[f['X']=='XYDATA'].index
    d2 = np.array(d1) + 1
    d3 = f[f['X']=='##### Extended Information'].index
    d3 = np.array(d3) - 1
    '''
    XDATA = f.iloc[1033:1780,0:1]
    YDATA = f.iloc[1033:1780,1:2]
    x = np.array(XDATA)
    y = np.array(YDATA) 
    x = [float(s) for s in x]
    y = [float(s) for s in y]
    x = np.array(x)
    y = np.array(y)

    return x,y

def plot(x1,y1,x2,y2):
    plt.plot(x1,y1,color='black',  linestyle='solid', linewidth = 2.0, label='line1')
    plt.plot(x2,y2,color='red',  linestyle='solid', linewidth = 2.0, label='line1')
    plt.title('Phthalonitrile in Ethanol',fontsize=16)
    plt.xlabel('Wave Number [cm-1]',fontsize=16) 
    plt.ylabel('Absorption [%]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.1)
    plt.show()

if __name__ == "__main__":

    file_BG = os.path.abspath('../../研究/yamada/20200827/BG_16scans_2.0cm_afternoon.csv')
    file_Solvent = os.path.abspath('../../研究/yamada/20200826/deg0_Abs_Ba2F_Acetone_12umSpacer_16scans_2.0cm.csv')
    file_Solute = os.path.abspath('../../研究/yamada/20200827/Phthalonitrile_in_ethanol/deg0_signal_Ba2F_Ethanol_12umSpacer_16scans_2.0cm.csv')

    #file = 'aa.csv'

    x1,y1 = data_change(file_BG)
    x2,y2 = data_change(file_Solvent)
    x3,y3 = data_change(file_Solute)
    #x4,y4 = data_change(file)
    #print(y4)
    #x4,y4 = x1[::],y1[::10]
    #print(x1)
    #print(y1)
    z = np.polyfit(x4,y4,70)
    print(z)
    a = np.poly1d(z)
    a = a(x4)
    print(a)
    plot(x4,a,x4,y4)


import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import argparse
import baseline_correction as bc
import polyfit as pl
import smoothing as sm

def data_change(file):
    f = pd.read_csv(file,encoding='Shift-JIS')
    f.columns=list('XY')

    d1 = f[f['X']=='XYDATA'].index
    d2 = np.array(d1) + 1
    d3 = f[f['X']=='##### Extended Information'].index
    d3 = np.array(d3) - 1

    XDATA = f.iloc[d2[0]:d3[0],0:1]
    YDATA = f.iloc[d2[0]:d3[0],1:2]
    x = np.array(XDATA)
    y = np.array(YDATA) 
    x = [float(s) for s in x]
    y = [float(s) for s in y]
    x = np.array(x)
    y = np.array(y)

    return x,y

def plot_Single(x,y):
    plt.plot(x,y,color='black',  linestyle='solid', linewidth = 2.0, label='only water')
    #plt.plot(x3,y3,color='red',  linestyle='solid', linewidth = 2.0, label='water + PH3')
    #plt.plot(clf)
    plt.title('Potassium Hexacyanoferrate',fontsize=16)
    plt.xlabel('Wave Number [cm-1]',fontsize=16) 
    plt.ylabel('Singlebeam [%]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.1)
    plt.legend()
    plt.show()

def plot_Trans(x,y):
    plt.plot(x,y,color='black',  linestyle='solid', linewidth = 2.0, label='only water')
    #plt.plot(x3,y3,color='red',  linestyle='solid', linewidth = 2.0, label='water + PH3')
    #plt.plot(clf)
    plt.title('Potassium Hexacyanoferrate',fontsize=16)
    plt.xlabel('Wave Number [cm-1]',fontsize=16) 
    plt.ylabel('Transmittance [%]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.1)
    plt.legend()
    plt.show()

def plotAbs(x,y,bkg,fix):
    plt.plot(x,y,color='black',  linestyle='solid', linewidth = 2.0, label='only water')
    ax1 = plt.subplot2grid((2,2), (0,0), colspan=2)
    ax2 = plt.subplot2grid((2,2), (1,0), colspan=2)
    ax1.plot(x, y, linewidth=2)
    ax1.plot(x, bkg, "b", linewidth=1, linestyle = "dashed", label="baseline")
    ax2.plot(x, fix, "r", linewidth=1, linestyle = "solid", label="remove baseline")
    plt.title('Potassium Hexacyanoferrate',fontsize=16)
    plt.xlabel('Wave Number [cm-1]',fontsize=16) 
    plt.ylabel('Absorbance [%]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.1)
    plt.legend()
    plt.show()

def parse_args():
    parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')    # 2. パーサを作る

    # 3. parser.add_argumentで受け取る引数を追加していく
    parser.add_argument('-base', help='baseline_correction.py')    # 必須の引数を追加
    parser.add_argument('-smooth', help='smoothing.py')
    parser.add_argument('-poly', help='polyfit.py')    # オプション引数（指定しなくても良い引数）を追加

    return parser.parse_args()    # 4. 引数を解析



if __name__ == "__main__":

    file_BG = os.path.abspath('../../研究/yamada/20200827/BG_16scans_2.0cm_afternoon.csv')
    file_Solvent = os.path.abspath('../../研究/yamada/20200826/deg0_Abs_Ba2F_Acetone_12umSpacer_16scans_2.0cm.csv')
    file_Solute = os.path.abspath('../../研究/yamada/20200827/Phthalonitrile_in_ethanol/deg0_signal_Ba2F_Ethanol_12umSpacer_16scans_2.0cm.csv')

    x1,y1 = data_change(file_BG)
    x2,y2 = data_change(file_Solvent)
    x3,y3 = data_change(file_Solute)
    #skip the data
    x, y = x2[::40],y2[::40]
    
    #実行します
    args = parse_args()
    if args.base:
        bc.outFigCSV(x,y)


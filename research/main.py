import csv
import numpy as np
import os
import pandas as pd
import argparse
import baseline_correction as bc
import smoothing as sm
import fitting as ft
import analyze as ana

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

def parse_args():
    parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')    # 2. パーサを作る

    # 3. parser.add_argumentで受け取る引数を追加していく
    parser.add_argument('-base', help='baseline_correction.py')    # 必須の引数を追加
    parser.add_argument('-smooth', help='smoothing.py')
    parser.add_argument('-fit', help='fitting.py')
    parser.add_argument('-ana1', help='analyze.py')
    parser.add_argument('-ana2', help='analyze.py')

    return parser.parse_args()    # 4. 引数を解析



if __name__ == "__main__":

    file_BG = os.path.abspath('../../研究/yamada/20200909/vacant_T_14nmAu_10umSpacer_16scans_2.0cm.csv')
    file_Solvent = os.path.abspath('../../研究/yamada/20200907/PH_in_Water_T_14nmAu_12umSpacer_16scans_2.0cm.csv')
    file_Solute = os.path.abspath('../../研究/yamada/20200909/PH_in_Water_T_14nmAu_10umSpacer_16scans_2.0cm.csv')

    x1,y1 = data_change(file_BG)
    x2,y2 = data_change(file_Solvent)
    x3,y3 = data_change(file_Solute)
    #skip the data
    #x1,y1 = x1[14229:14747],y2[14229:14747]
    #x3,y3 = x3[2510:5208],y3[2510:5208]
    x1, y1 = x1[::10],y1[::10]
    x2, y2 = x2[::10],y2[::10]
    x3, y3 = x3[::10],y3[::10]

    #実行します
    args = parse_args()
    if args.base:
        bc.outFigCSV(x2,y1,y2,y3)
    '''
    if args.smooth:
        bc.outFigCSV(x1,y1)
    if args.fit:
        ft.gauss_func(x,y)
    '''
    if args.ana1:
        ana.fit(x1,y1)
    
    if args.ana2:
        ana.fsr(x1,y1)

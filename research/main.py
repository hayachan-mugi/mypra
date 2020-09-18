# import current directry python files
import baseline_correction as bc
import smoothing as sm
import fitting as ft
import analyze as ana
import plot as pl
# import python library
import csv
import numpy as np
import os
import pandas as pd
import argparse


def data_change(file):
    f = pd.read_csv(file,encoding='Shift-JIS')
    f.columns=list('XY')

    d1 = f[f['X']=='XYDATA'].index
    d2 = np.array(d1) + 1
    d3 = f[f['X']=='##### Extended Information'].index
    d3 = np.array(d3) - 1

    XDATA = f.iloc[d2[0]:d3[0],0:1]
    YDATA = f.iloc[d2[0]:d3[0],1:5]
    x = np.array(XDATA)
    y = np.array(YDATA) 
    x = [float(s) for s in x]
    y = [float(s) for s in y]
    x = np.array(x)
    y = np.array(y)

    return x,y

def parse_args():
    parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')    # 5. パーサを作る

    # 5. parser.add_argumentで受け取る引数を追加していく
    parser.add_argument('-smooth', help='smoothing.py --smoothing deal')
    parser.add_argument('-anaLF', help='analyze.py --Lorentz_fit')
    parser.add_argument('-anaFSR', help='analyze.py --fsr')
    parser.add_argument('-anaN', help='analyze.py --reflective index')
    parser.add_argument('-plot', help='plot.py --only plot')

    return parser.parse_args()    # 5. 引数を解析



if __name__ == "__main__":

    args = parse_args()
    if args.anaN:
        ref_index = ana.reflective_index()
        print('Real reflective index(solution) :',ref_index)
        exit()
    
    # MY PC
    '''
    file_BG = os.path.abspath('../../../../奈良先端大研究/yamada/20200902/PH_in_Water/deg0_Abs_water_CaF2_12umSpacer_16scans_2.0cm.csv')
    file_Solvent = os.path.abspath('../../../../奈良先端大研究/yamada/20200909/vacant_T_14nmAu_10umSpacer_16scans_2.0cm.csv')
    file_Solute = os.path.abspath('../../../../奈良先端大研究/yamada/20200909/PH_in_Water_T_14nmAu_10umSpacer_16scans_2.0cm.csv')
    '''
    # Lab
    
    file_BG = os.path.abspath('../../研究/yamada/20200915/Water_T_14nmAu_6umSpacer_16scans_2.0cm.csv')
    file_Solvent = os.path.abspath('../../研究/yamada/20200909/PH_in_Water_T_14nmAu_10umSpacer_16scans_2.0cm.csv')
    file_Solute = os.path.abspath('../../研究/yamada/20200915/vacant_T_14nmAu_6umSpacer_16scans_2.0cm.csv')
    
    x1,y1 = data_change(file_BG)
    x3,y3 = data_change(file_Solvent)
    x2,y2 = data_change(file_Solute)

    #change the range of data 
    #x1,y1 = x1[2510:5208],y1[2510:5208]
    #x2,y2 = x2[2510:5208],y2[2510:5208]
    #x3,y3 = x3[2510:5208],y3[2510:5208]

    #skip the data(10step)
    fix_x1, fix_y1 = x1[::5],y1[::5]
    fix_x2, fix_y2 = x2[::5],y2[::5]
    fix_x3, fix_y3 = x3[::5],y3[::5]
    #baseline correction
    fix_x1,fix_y1,fix_y2,fix_y3 = bc.baseline(x1,y1,y2,fix_x1,fix_y1,fix_y2,fix_y3)


    #実行します
    
    if args.anaLF:
        ana.Lorentz_fit(fix_x2,fix_y2)
    
    if args.anaFSR:
        ana.fsr(fix_x1,fix_y2)
    
    if args.plot:
        pl.Trans(fix_x1,fix_y1,fix_y2,fix_y3)
    
    '''
    if args.smooth:
        bc.outFigCSV(x1,y1)

    '''

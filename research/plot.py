import matplotlib.pyplot as plt
import os
import numpy as np

save_dir = '../../研究/M1/週報/9月/' #ファイルを保存したいディレクトリ

def Single(x1,y1,y2,y3):
    #fig = plt.figure()
    plt.plot(x1,y1,color='black',  linestyle='solid', linewidth = 2.0, label='only water')
    #plt.plot(x3,y3,color='red',  linestyle='solid', linewidth = 2.0, label='water + PH3')
    plt.title('Potassium Hexacyanoferrate',fontsize=16)
    plt.xlabel('Wave Number [cm-1]',fontsize=16) 
    plt.ylabel('Singlebeam [%]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.1)
    plt.legend()
    plt.show()
    #fig.savefig(os.path.join(save_dir, '0910_S_PH3+water.png'))

def Trans(x,y1,y2,y3):
    #fig = plt.figure()
    #plt.plot(x,y1,color='black',  linestyle='solid', linewidth = 2.0, label='vacant')
    plt.plot(x,y1,color='red',  linestyle='solid', linewidth = 2.0, label='Spacer:12um')
    plt.scatter(y2,y3)
    plt.title('Potassium Hexacyanoferrate',fontsize=16)
    plt.xlabel('Wave Number [cm-1]',fontsize=16) 
    plt.ylabel('Transmittance [%]',fontsize=16) 
    plt.xlim()
    plt.ylim()
    plt.grid(color='b', linestyle='--', linewidth=0.2)
    plt.legend()
    plt.show()
    #fig.savefig(os.path.join(save_dir, '0910_T_PH3+water.png')) #plt.saveig()でグラフを保存 #これで別ディレクトリsave_dir内にグラフ'hoge.png'が保存された


def Abs(x1,y1,y2,y3):
    #fig = plt.figure()
    ax1 = plt.subplot2grid((2,2), (0,0), colspan=5)
    ax2 = plt.subplot2grid((2,2), (1,0), colspan=2)
    ax1.plot(x1, y1, linewidth=2)
    ax1.plot(x1, y2, "b", linewidth=1, linestyle = "dashed", label="baseline")
    ax2.plot(x1, y3, "r", linewidth=2, linestyle = "solid", label="remove baseline")
    '''
    ax1.xlabel('Wave Number [cm-1]',fontsize=16) 
    ax1.ylabel('Absorbance [%]',fontsize=16) 
    ax2.xlabel('Wave Number [cm-1]',fontsize=16) 
    ax2.ylabel('Absorbance [%]',fontsize=16)
    ''' 
    plt.xlim()
    plt.ylim()
    ax1.grid(color='b', linestyle='--', linewidth=0.1)
    ax1.legend()
    ax2.grid(color='b', linestyle='--', linewidth=0.1)
    ax2.legend()
    plt.show()
    #fig.savefig(os.path.join(save_dir, '0910_A_PH3+water.png'))
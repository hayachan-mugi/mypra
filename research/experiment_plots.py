import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


#convert to absorption
def convert_cal(x1,y1,x2,y2):
    y = y1/y2
    y = np.log(y)
    print(y)
    if x1.all() == x2.all():
        return x1,y
    else :
        return False

#plot function
def plot(x,y):
    plt.plot(x,y)
    plt.show()


if __name__ == "__main__":

    file1 = input('Enter Background Filename : ')
    file2 = input('Enter Sample Filename : ')
    x1,y1 = data_change(file1)
    x2,y2 = data_change(file2)
    x,y = convert_cal(x1,y1,x2,y2)
    plot(x,y)


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = input('Enter filename : ')
f = pd.read_csv(file,encoding='Shift-JIS')

f.columns=list('AB')
d1 = f[f['A']=='XYDATA'].index
d2 = np.array(d1) + 1
d3 = f[f['A']=='##### Extended Information'].index
d3 = np.array(d3) - 1

XDATA = f.iloc[d2[0]:d3[0],0:1]
YDATA = f.iloc[d2[0]:d3[0],1:2]

x = np.array(XDATA)
y = np.array(YDATA)
x = [float(s) for s in x]
y = [float(s) for s in y]
x = np.array(x)
y = np.array(y)

#convert 赤外線
h = x/y
h = np.log(h)
print(h)


plt.plot(x,y)
plt.show()



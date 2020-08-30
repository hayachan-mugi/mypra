import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import collections
import math
def flatten(l):
    for el in l:
        if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

file = "BG_16scans_2.0cm_morning.csv"
lines = []
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


'''x = x.tolist()
y = y.tolist()
x = list(flatten(x))
y = list(flatten(y)) 
'''
'''
for i in range(len(x)):
     a = x[i] + y[i]
     a = np.append(a)
print(a)
'''
plt.plot(x,h)
plt.show()

'''with open(file, "r", encoding = "Shift-JIS") as f:
    rows = csv.reader(f)
    print(type(rows))
    print(rows)
    for row in rows:
        lines.append(row)
'''
    #d = lines[18:20,0:2]
    #print(d)
#fileobj.columns=list('AB')
#d = fileobj['A'].isnull()
#g = fileobj.iloc[:,:].isnull()
#y=g.values
 #   for row in fileobj:
  #     print('a')

#print(len(y))
#if y.all() == False:

#print(fileobj['A'].isnull())
'''
#print(len(df.iloc[:,0:1]))
print(df)
t=df.values
print(df.values)
#if t==t[True][True]:
 #   print(t)
'''
'''
    while True :
        line = f.readline()[20:]
        print(line)
        break

#print(wave_num)

#with codecs.open("vacant_T_Ba2F_12umSpacer_16scans_2.0cm.csv", "r", "Shift-JIS", "ignore") as file:
# data = pd.read_table(file, delimiter=",")

#df = data.iloc[0:4,20:]
#print(df)
'''
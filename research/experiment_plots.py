import csv
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import codecs
import numpy as np

file = "vacant_T_Ba2F_12umSpacer_16scans_2.0cm.csv"

#fileobj = pd.read_csv(file,encoding='Shift-JIS')
with open(file, "r", encoding = "Shift-JIS") as fileobj:
#fileobj.columns=list('AB')
#d = fileobj['A'].isnull()
#g = fileobj.iloc[:,:].isnull()
#y=g.values
 #   for row in fileobj:
  #     print('a')
    print(fileobj[0:15,:])
#print(len(y))
#if y.all() == False:
    
print('aa')

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
#print(df)--#
'''
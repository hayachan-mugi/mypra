import csv
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import codecs

file = "vacant_T_Ba2F_12umSpacer_16scans_2.0cm.csv"
with open(file, "r", encoding = "Shift-JIS") as fileobj:
    f = fileobj.drop(0,axis=0)
    while True :
        line = f.readline()[20:]
        print(line)
        break

#print(wave_num)

#with codecs.open("vacant_T_Ba2F_12umSpacer_16scans_2.0cm.csv", "r", "Shift-JIS", "ignore") as file:
# data = pd.read_table(file, delimiter=",")

#df = data.iloc[0:4,20:]
#print(df)--#


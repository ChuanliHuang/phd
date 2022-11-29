import pandas as pd
import scipy.stats
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220126_Bub1 vs peri-CEN boarder/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
df_1 = df.copy()
# verify l1 and l2
for cell in range(len(df['cell'].unique())):
    for time in range(len(df['time'].unique())):
        selection1 = df[(df['cell']==cell+1)&(df['time']==time+1)&(df['l']==1)]['distance']
        selection2 = df[(df['cell']==cell+1)&(df['time']==time+1)&(df['l']==2)]['distance']
        l1 = selection1.values[0]
        l2 = selection2.values[0]
        row1 = selection1.index[0]
        row2 = selection2.index[0]
        if l1 > l2:
            df_1.iloc[row1, 3] = l2
            df_1.iloc[row2, 3] = l1

# make lists for l1 and l2
df = df_1
l1_ls = []
l2_ls = []
l_ls = []
for i in range(len(df['cell'].unique())):
    bub1_d = df[(df['cell'] == i+1)&(df['l'] == 0)]['distance']
    l1 = df[(df['cell'] == i+1)&(df['l'] == 1)]['distance']
    for x in l1[list(bub1_d != 0)].to_numpy():
        if x > 0:
            l1_ls.append(x)
    l2 = df[(df['cell'] == i+1)&(df['l'] == 2)]['distance']
    for x in l2[list(bub1_d != 0)].to_numpy():
        if x > 0:
            l2_ls.append(x)
    for x in l1[list(bub1_d == 0)]:
        l_ls.append(x)

print(l1_ls)
print(scipy.stats.describe(l1_ls))
print(np.median(l1_ls))
print(l2_ls)
print(scipy.stats.describe(l2_ls))
print(np.median(l2_ls))
print(l_ls)
print(scipy.stats.describe(l_ls))
print(np.median(l_ls))
l1l2_ls = l1_ls + l2_ls
print(l1l2_ls)
print(scipy.stats.describe(l1l2_ls))
print(np.median(l1l2_ls))
# print(l1_ls)
# print(l2_ls)
# print(l_ls)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220126_Bub1 vs peri-CEN boarder/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
df_1 = df.copy()


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

# interKT > 0
df = df_1
bub1_d_ls = []
l1_ls = []
l2_ls = []
for i in range(len(df['cell'].unique())):
    bub1_d = df[(df['cell'] == i+1)&(df['l'] == 0)]['distance']
    l1 = df[(df['cell'] == i+1)&(df['l'] == 1)]['distance']
    l2 = df[(df['cell'] == i+1)&(df['l'] == 2)]['distance']
    for x in bub1_d[list(bub1_d != 0)].to_numpy():
        if x > 0:
            bub1_d_ls.append(x)
    for x in l1[list(bub1_d != 0)].to_numpy():
        if x > 0:
            l1_ls.append(x)
    for x in l2[list(bub1_d != 0)].to_numpy():
        if x > 0:
            l2_ls.append(x)
bub1_d_arr = np.array(bub1_d_ls)
l1_arr = np.array(l1_ls)
l2_arr = np.array(l2_ls)
plt.plot(bub1_d_arr, l1_arr, '.')
plt.plot(bub1_d_arr, l2_arr, '.')
# l1
x = bub1_d_arr.reshape(-1, 1)
y = l1_arr
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
x = np.linspace(min(bub1_d_arr), max(bub1_d_arr), 100)
y = model.coef_[0] * x + model.intercept_
plt.plot(x, y, color='tab:blue', alpha=0.5, label=r'$L1$ $R^2$ = {}'.format(round(r_sq, 2)))
# l2
x = bub1_d_arr.reshape(-1, 1)
y = l2_arr
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
x = np.linspace(min(bub1_d_arr), max(bub1_d_arr), 100)
y = model.coef_[0] * x + model.intercept_
plt.plot(x, y, color='tab:orange', alpha=0.5, label=r'$L2$ $R^2$ = {}'.format(round(r_sq, 2)))



plt.ylim(-0.05, 1.305)
plt.xlabel(r'distance$_{interKT}$ ($\mu$m)')
plt.yticks([])
plt.legend()
plt.show()

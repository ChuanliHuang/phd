import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220124_Bub1-mNG_Mtw1-td/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

x = []
y = []

for cell in df['cell'].unique():
    selection = df['cell'] == cell
    g_int = df[selection]['g_intensity']
    r_distance = df[selection]['r_distance']
    selected_index = []
    for i in range(len(g_int)):
        if 0 < r_distance.values[i] < 2:
            selected_index.append(i)
    selected_index.append(int(selected_index[0]) - 1)
    r_distance = r_distance.values[selected_index]
    g_int = g_int.values[selected_index]
    for j in r_distance:
        x.append(j)
    for j in g_int:
        y.append(j)
plt.plot(x, y, '.')
x = np.array(x)
x = x.reshape(-1, 1)
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
x = np.linspace(min(x), max(x), 100)
y = model.coef_[0] * x + model.intercept_
plt.plot(x, y, color='tab:blue', alpha=0.5, label=r'$R^2$ = {}'.format(round(r_sq, 2)))
plt.xlabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylabel('KT Bub1-mNG intensity (a.u.)')
plt.legend()
plt.show()
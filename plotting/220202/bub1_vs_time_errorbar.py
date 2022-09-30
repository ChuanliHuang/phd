from scipy.stats import sem
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220124_Bub1-mNG_Mtw1-td/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
x = []
y = []
yerrs = []
for time in df['time'].unique():
    selection = df['time'] == time
    x.append((time - 1) * 10 + 20)
    g_int_mean = df[selection]['g_intensity'].mean()
    yerr = sem(df[selection]['g_intensity'])
    yerrs.append(yerr)
    y.append(g_int_mean)

plt.errorbar(x, y, yerr=yerrs, color='tab:green', linewidth=2)

# plt.legend(loc=1)
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
# plt.xticks(np.arange(20, 160, step=10), ('20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120'))
plt.xlabel(r'time after G1 release (min)')
plt.ylabel('KT Bub1-mNG intensity (a.u.)')
# plt.ylim(-15, 255)
# plt.xlim(10, 170)
plt.show()
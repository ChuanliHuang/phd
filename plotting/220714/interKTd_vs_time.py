import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220714_Bub1-mNG_glc7-12/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']
glc7_12_df = df[df['strain'] == 'glc7-12']

for cell in wt_df['cell'].unique():
    selection = wt_df['cell'] == cell
    time = wt_df[selection]['time'] * 15 + 15
    r_distance = wt_df[selection]['r_distance']
    plt.plot(time, r_distance, '.', color='tab:blue', alpha=0.3)
x = []
y = []
for time in wt_df['time'].unique():
    selection = wt_df['time'] == time
    x.append(time * 15 + 15)
    g_int_median = wt_df[selection]['r_distance'].median()
    y.append(g_int_median)
plt.plot(x, y, color='tab:blue', linewidth=2, label='wild type')

for cell in glc7_12_df['cell'].unique():
    selection = glc7_12_df['cell'] == cell
    time = glc7_12_df[selection]['time'] * 15 + 15
    r_distance = glc7_12_df[selection]['r_distance']
    plt.plot(time, r_distance, '.', color='tab:orange', alpha=0.3)
x = []
y = []
for time in glc7_12_df['time'].unique():
    selection = glc7_12_df['time'] == time
    x.append(time * 15 + 15)
    g_int_median = glc7_12_df[selection]['r_distance'].median()
    y.append(g_int_median)
plt.plot(x, y, color='tab:orange', linewidth=2, label=r'$\it{glc7-12}$')

plt.legend(loc=1)
plt.xticks(np.arange(30, 195, step=15), ('30', '45', '60', '75', '90', '105', '120', '135', '150', '165', '180'))
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylim(-0.05, 2.55)
plt.show()
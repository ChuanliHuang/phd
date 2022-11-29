import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np


file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220508_Bub1-mNG_met-SCC1_pre-cleaned/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']
metscc1_df = df[df['strain'] == 'met-SCC1']

for cell in wt_df['cell'].unique():
    selection = wt_df['cell'] == cell
    time = wt_df[selection]['time'] * 15
    r_distance = wt_df[selection]['r_distance']
    plt.plot(time, r_distance, '.', color='tab:blue', alpha=0.3)
x = []
y = []
for time in wt_df['time'].unique():
    selection = wt_df['time'] == time
    x.append(time * 15)
    g_int_median = wt_df[selection]['r_distance'].median()
    y.append(g_int_median)
plt.plot(x, y, color='tab:blue', linewidth=2, label='wild type')

for cell in metscc1_df['cell'].unique():
    selection = metscc1_df['cell'] == cell
    time = metscc1_df[selection]['time'] * 15
    r_distance = metscc1_df[selection]['r_distance']
    plt.plot(time, r_distance, '.', color='tab:orange', alpha=0.3)
x = []
y = []
for time in metscc1_df['time'].unique():
    selection = metscc1_df['time'] == time
    x.append(time * 15)
    g_int_median = metscc1_df[selection]['r_distance'].median()
    y.append(g_int_median)
plt.plot(x, y, color='tab:orange', linewidth=2, label='pMET-SCC1')

plt.legend(loc=1)
plt.xlabel(r'time after release from G1 (min)')
plt.xticks(np.arange(15, 180, step=15), ('15', '30', '45', '60', '75', '90', '105', '120', '135', '150', '165'))
plt.ylabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylim(-0.1, 4.05)
plt.show()


# plt.savefig('/Users/kikawaryoku/Desktop/fig1.png')
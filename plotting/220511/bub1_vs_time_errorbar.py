from scipy.stats import sem
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np


file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220508_Bub1-mNG_met-SCC1_pre-cleaned/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']
metscc1_df = df[df['strain'] == 'met-SCC1']
# for cell in wt_df['cell'].unique():
#     selection = wt_df['cell'] == cell
#     time = wt_df[selection]['time'] * 15
#     g_int = wt_df[selection]['g_intensity']
#     plt.plot(time, g_int, '.', color='tab:blue', alpha=0.3)
x = []
y = []
yerrs = []
for time in wt_df['time'].unique():
    selection = wt_df['time'] == time
    x.append(time * 15)
    g_int_mean = wt_df[selection]['g_intensity'].mean()
    yerr = sem(wt_df[selection]['g_intensity'])
    yerrs.append(yerr)
    y.append(g_int_mean)

plt.errorbar(x, y, yerr=yerrs, color='tab:blue', linewidth=2, label='wild type')

x = []
y = []
yerrs = []
for time in metscc1_df['time'].unique():
    selection = metscc1_df['time'] == time
    x.append(time * 15)
    g_int_mean = metscc1_df[selection]['g_intensity'].mean()
    yerr = sem(metscc1_df[selection]['g_intensity'])
    yerrs.append(yerr)
    y.append(g_int_mean)

plt.errorbar(x, y, yerr=yerrs, color='tab:orange', linewidth=2, label=r'$pMET-SCC1$')


plt.legend(loc=1)
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel('KT Bub1-mNG intensity (a.u.)')
plt.xticks(np.arange(15, 180, step=15), ('15', '30', '45', '60', '75', '90', '105', '120', '135', '150', '165'))
plt.ylim(-15, 255)
plt.show()
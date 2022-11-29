import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220508_Bub1-mNG_met-SCC1_pre-cleaned/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']

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
plt.plot(x, y, color='tab:blue', linewidth=2, label='BUB1-mNG')


file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220507_Sgo1-EGFP_H2A_mutants/data.xlsx'
df = pd.read_excel(file_name, sheet_name=1)
wt_df = df[df['strain'] == 'wt']
wt_median = [wt_df[i].median() for i in range(15, 180, 15)]

for i, row in wt_df.iterrows():
    plt.plot(range(15, 180, 15), row[3:], '.', color='tab:orange', alpha=0.3)

plt.plot(np.arange(15, 180, 15), wt_median, color='tab:orange', linewidth=2, label='SGO1-EGFP')
plt.xticks(np.arange(15, 180, step=15), ('15', '30', '45', '60', '75', '90', '105', '120', '135', '150', '165'))
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylim(-0.05, 2.55)
plt.legend(loc=1)

plt.show()
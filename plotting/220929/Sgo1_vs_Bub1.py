import pandas as pd
from scipy.stats import sem
import matplotlib.pyplot as plt
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220929_Sgo1-EGFP_in_met-Scc1/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
sgo1_df = df[df['strain'] == 'wt']

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220508_Bub1-mNG_met-SCC1_pre-cleaned/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
bub1_df = df[df['strain'] == 'wt']

x = []
y = []
yerrs = []
for time in bub1_df['time'].unique():
    selection = bub1_df['time'] == time
    x.append(time * 15)
    g_int_mean = bub1_df[selection]['g_intensity'].mean()
    yerr = sem(bub1_df[selection]['g_intensity'])
    yerrs.append(yerr)
    y.append(g_int_mean)

sgo1 = [sgo1_df[i].sum()/sgo1_df[i].count() for i in range(15, 180, 15)]


# create figure and axis objects with subplots()
fig, ax = plt.subplots()
# make a plot
ax.plot(x, y, '-o', color='tab:blue')
# set x-axis label
ax.set_xlabel(r'time after G1 release (min)')
# set y-axis label
ax.set_ylabel('mean KT Bub1-mNG intensity (a.u.)', color='tab:blue')
ax.tick_params(axis='y', colors='tab:blue')

# twin object for two different y-axis on the sample plot
ax2 = ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(x, sgo1, '-o', color='tab:orange')
ax2.set_ylabel(r'% Cells with Sgo1-EGFP dot(s)', color='tab:orange')
ax2.set_yticks(np.arange(0, 1.2, step=0.2), ('0%', '20%', '40%', '60%', '80%', '100%'))
ax2.spines['left'].set_color('tab:blue')
ax2.spines['right'].set_color('tab:orange')
ax2.tick_params(axis='y', colors='tab:orange')

plt.xticks(range(15, 180, 15), ('15', '30', '45', '60', '75', '90', '105', '120', '135', '150', '165'))
plt.show()
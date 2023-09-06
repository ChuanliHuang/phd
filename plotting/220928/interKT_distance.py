import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np
import seaborn as sns

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220928_Sgo1-EGFP_in_rts1_mutants/data.xlsx'
df = pd.read_excel(file_name, sheet_name=1)
wt_df = df[df['strain'] == 'wt']
rts1d_df = df[df['strain'] == 'rts1d']
sgo1_3A_df = df[df['strain'] == 'sgo1-3A']

wt_median = [wt_df[i].median() for i in range(30, 195, 15)]
rts1d_median = [rts1d_df[i].median() for i in range(30, 195, 15)]
sgo1_3A_median = [sgo1_3A_df[i].median() for i in range(30, 195, 15)]


for i, row in wt_df.iterrows():
    plt.plot(range(30, 195, 15), row[3:], '.', color='tab:blue', alpha=0.3)

for i, row in rts1d_df.iterrows():
    plt.plot(range(30, 195, 15), row[3:], '.', color='tab:orange', alpha=0.3)

for i, row in sgo1_3A_df.iterrows():
    plt.plot(range(30, 195, 15), row[3:], '.', color='tab:green', alpha=0.3)

plt.plot(np.arange(30, 195, 15), wt_median, linewidth=2, label=r'wild type')
plt.plot(np.arange(30, 195, 15), rts1d_median, linewidth=2, label=r'$\it{rts1\Delta}$')
plt.plot(np.arange(30, 195, 15), sgo1_3A_median, linewidth=2, label=r'$\it{sgo1-3A}$')
plt.xticks(np.arange(30, 195, step=15), ('30', '45', '60', '75', '90', '105', '120', '135', '150', '165', '180'))
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylim(-0.25, 2.55)
plt.legend()
plt.show()
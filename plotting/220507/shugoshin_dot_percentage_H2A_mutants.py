import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220507_Sgo1-EGFP_H2A_mutants/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']
S121D_df = df[df['strain'] == 'S121D']
S121A_df = df[df['strain'] == 'S121A']

wt = [wt_df[i].sum()/wt_df[i].count() for i in range(15, 180, 15)]
# wt = [0] + wt[:-1]
S121D = [S121D_df[i].sum()/S121D_df[i].count() for i in range(15, 180, 15)]
S121A = [S121A_df[i].sum()/S121A_df[i].count() for i in range(15, 180, 15)]

plt.plot(wt, '-D', label='wild type')
# plt.plot(S121D, '--o', label=r'$\it{hta1-S121D}$')
plt.plot(S121A, '--o', label=r'H2A-S121A')
plt.plot(S121D, ':*', label=r'H2A-S121D')
plt.xticks(np.arange(0, 11, step=1), ('15', '30', '45', '60', '75', '90', '105', '120', '135', '150', '165'))
plt.yticks(np.arange(0, 1.2, step=0.2), ('0', '20', '40', '60', '80', '100'))
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'% Cells with Sgo1-EGFP dot(s)')
plt.ylim(-0.05, 1.05)

plt.legend()
plt.show()
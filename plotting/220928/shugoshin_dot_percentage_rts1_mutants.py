import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220928_Sgo1-EGFP_in_rts1_mutants/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']
rts1d_df = df[df['strain'] == 'rts1d']
sgo1_3A_df = df[df['strain'] == 'sgo1-3A']

wt = [wt_df[i].sum()/wt_df[i].count() for i in range(30, 195, 15)]
rts1d = [rts1d_df[i].sum()/rts1d_df[i].count() for i in range(30, 195, 15)]
sgo1_3A = [sgo1_3A_df[i].sum()/sgo1_3A_df[i].count() for i in range(30, 195, 15)]

plt.plot(wt, '-o', label='wild type')
plt.plot(rts1d, '-o', label=r'$\it{rts1\Delta}$')
plt.plot(sgo1_3A, '-o', label=r'$\it{sgo1-3A}$')
plt.xticks(np.arange(0, 11, step=1), ('30', '45', '60', '75', '90', '105', '120', '135', '150', '165', '180'))
plt.yticks(np.arange(0, 1.2, step=0.2), ('0', '20', '40', '60', '80', '100'))
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'% Cells with Sgo1-EGFP dot(s)')
plt.ylim(-0.05, 1.05)

plt.legend()
plt.show()
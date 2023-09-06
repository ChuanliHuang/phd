import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220929_Sgo1-EGFP_in_met-Scc1/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']
met_scc1_df = df[df['strain'] == 'met-SCC1']

wt = [wt_df[i].sum()/wt_df[i].count() for i in range(15, 180, 15)]
met_scc1 = [met_scc1_df[i].sum()/met_scc1_df[i].count() for i in range(15, 180, 15)]


plt.plot(wt, '-o', label='wild type')
plt.plot(met_scc1, '-o', label=r'$pMET-SCC1$')
plt.xticks(np.arange(0, 11, step=1), ('15', '30', '45', '60', '75', '90', '105', '120', '135', '150', '165'))
plt.yticks(np.arange(0, 1.2, step=0.2), ('0%', '20%', '40%', '60%', '80%', '100%'))
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'% Cells with Sgo1-EGFP dot(s)')
plt.ylim(-0.05, 1.05)

plt.legend(loc='upper left')
plt.show()
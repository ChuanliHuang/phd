import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import math
import numpy as np

# this file is generated from codes in folder Marston2013 of Alex Barr's github
file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_ChIP_data_analysis/070922_pH2A ChIP-seq_00/data/Arm50kb.xlsx'

tension_df = pd.read_excel(file_name, sheet_name=0, header=None, usecols='A:AX')
no_tension_df = pd.read_excel(file_name, sheet_name=1, header=None)
# print(tension_df)
# print(no_tension_df)

tension_means = tension_df.mean(axis=1, skipna=True)
tension_stds = tension_df.std(axis=1, skipna=True)
tension_cis = 1.96 * tension_stds/np.sqrt(16)
tension_means = tension_means.values.tolist()
tension_cis = tension_cis.values.tolist()
tension_means_log2 = [math.log2(x) for x in tension_means]
tension_lower = [tension_means[i] - tension_cis[i] for i in range(len(tension_means))]
tension_lower_log2 = [math.log2(x) for x in tension_lower]
tension_upper = [tension_means[i] + tension_cis[i] for i in range(len(tension_means))]
tension_upper_log2 = [math.log2(x) for x in tension_upper]


no_tension_means = no_tension_df.mean(axis=1, skipna=True)
no_tension_stds = no_tension_df.std(axis=1, skipna=True)
no_tension_cis = 1.96 * no_tension_stds/np.sqrt(16)
no_tension_means = no_tension_means.values.tolist()
no_tension_means_log2 = [math.log2(x) for x in no_tension_means]
no_tension_lower = [no_tension_means[i] - no_tension_cis[i] for i in range(len(no_tension_means))]
no_tension_lower_log2 = [math.log2(x) for x in no_tension_lower]
no_tension_upper = [no_tension_means[i] + no_tension_cis[i] for i in range(len(no_tension_means))]
no_tension_upper_log2 = [math.log2(x) for x in no_tension_upper]

x = [(i-250)/10 for i in range(len(tension_means_log2))]

plt.plot(x, tension_means_log2, label='tension')
plt.plot(x, no_tension_means_log2, label='no tension')
plt.fill_between(x, tension_lower_log2, tension_upper_log2, color='tab:blue', alpha=.1)
plt.fill_between(x, no_tension_lower_log2, no_tension_upper_log2, color='tab:orange', alpha=.1)
plt.xlabel('distance (kb)')
plt.ylabel(r'log$_{2}$ (mean calibrated RPM)')
plt.title('Chromosome arm')
plt.ylim(2, 13)
plt.legend()
plt.show()
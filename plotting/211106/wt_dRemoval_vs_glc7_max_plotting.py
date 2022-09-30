import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statannot import add_stat_annotation



file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/211105_Sgo1-EGFP_glc7-12_34C_quantification/removal_vs_max.csv'
df = pd.read_csv(file_name)
print(df)
# fig, ax = plt.subplots(figsize=(16, 4.8))
# ax = sns.swarmplot(x="type", y="value", data=df, color='tab:red', size=2)
ax = sns.swarmplot(x="type", y="value", data=df, size=2)
ax = sns.pointplot(x="type", y="value", data=df, estimator=np.mean, ci=None, join=False, markers='d', scale=0.6, color='0.25')
plt.setp(ax.lines, zorder=100)
plt.setp(ax.collections, zorder=100)
plt.setp(ax.collections[-1], label='mean')
ax.set(ylabel=r"$Sgo1_{peri-CEN}$ (min)")


add_stat_annotation(ax, data=df, x='type', y='value',
                    box_pairs=[('wt_removal', 'glc7_max')],
                    test='t-test_ind', text_format='star', loc='outside', verbose=2)

plt.xticks(np.arange(0, 2, 1), (r'wild type$_{removal}$', r'$\it{glc7-12}_{maximum}$'))
plt.ylabel(r'distance$_{interKT}$ ($\mu$m)')
plt.xlabel('')
plt.legend()
plt.show()
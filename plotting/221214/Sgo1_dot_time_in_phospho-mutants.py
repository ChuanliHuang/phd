import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np
from statannot import add_stat_annotation


sns.set(style='whitegrid')
file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/221214_Sgo1-EGFP_in_phospho-mutants/Exp11_b_Sgo_dot_time/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
ax = sns.swarmplot(x="strain", y="duration", data=df, size=4)
ax = sns.pointplot(x="strain", y="duration", data=df, estimator=np.median, ci=None, join=False, markers='d', scale=0.6, color='0.25')
plt.setp(ax.lines, zorder=100)
plt.setp(ax.collections, zorder=100)
plt.setp(ax.collections[-1], label='median')
ax.set(ylabel="time Sgo1-EGFP as foci (mins)")
add_stat_annotation(ax, data=df, x='strain', y='duration',
                    box_pairs=[("wt", "rts1d"), ('wt', 'S421A'), ('wt', 'S421D'), ('wt', 'S487A'), ('wt', 'S487D')],
                    test='Mann-Whitney', text_format='star', loc='outside', verbose=2)
plt.xticks(np.arange(0, 6, 1), ('wild type', r'$\it{rts1\Delta}$', r'$\it{sgo1-S421A}$', r'$\it{sgo1-S421D}$', r'$\it{sgo1-S487A}$', r'$\it{sgo1-S487D}$'), rotation=45)
plt.yticks(np.arange(20, 100, step=10), ('20', '30', '40', '50', '60', '70', '80', '>80'))
plt.xlabel('')
plt.legend()
plt.show()
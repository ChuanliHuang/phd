import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np
from statannot import add_stat_annotation


sns.set(style='whitegrid')
file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/221214_Sgo1-EGFP_in_phospho-mutants/fluo/fluo_intensity.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
ax = sns.swarmplot(x="strain", y="g", data=df, size=4)
ax = sns.pointplot(x="strain", y="g", data=df, estimator=np.median, ci=None, join=False, markers='d', scale=0.6, color='0.25')
plt.setp(ax.lines, zorder=100)
plt.setp(ax.collections, zorder=100)
plt.setp(ax.collections[-1], label='median')
ax.set(ylabel="Sgo1-EGFP foci fluorescence intensity (a.u.)")
add_stat_annotation(ax, data=df, x='strain', y='g',
                    box_pairs=[("wt", "rts1d")],
                    test='t-test_ind', text_format='star', loc='outside', verbose=2)
plt.xticks(np.arange(0, 2, 1), ('wild type', r'$\it{rts1\Delta}$'))
# plt.yticks(np.arange(20, 100, step=10), ('20', '30', '40', '50', '60', '70', '80', '>80'))
plt.xlabel('')
plt.legend()
plt.show()
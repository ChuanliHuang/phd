import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statannot import add_stat_annotation


sns.set(style='whitegrid')
file_name = '/Users/kikawaryoku/Desktop/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
ax = sns.swarmplot(x="strain", y="meta_dur", data=df)
ax = sns.pointplot(x="strain", y="meta_dur", data=df, estimator=np.median, ci=None, join=False, color='0.25')
plt.setp(ax.lines, zorder=100)
plt.setp(ax.collections, zorder=100, label="")
ax.set(ylabel="metaphase duration (min)")
# add_stat_annotation(ax, data=df, x='strain', y='meta_dur',
#                     box_pairs=[("WT", "S+R"), ("WT", "S"), ("WT", "R")],
#                     test='Mann-Whitney', text_format='star', loc='outside', verbose=2)
plt.yticks(np.arange(0, 100, step=10), ('0', '10', '20', '30', '40', '50', '60', '70', '80', '>80'))
plt.show()


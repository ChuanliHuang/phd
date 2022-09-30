import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statannot import add_stat_annotation


# sns.set(style='whitegrid')
file_name = '/Users/kikawaryoku/Desktop/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
# fig, ax = plt.subplots(figsize=(16, 4.8))
ax = sns.swarmplot(x="strain", y="sum", data=df, color='green', size=2)
ax = sns.pointplot(x="strain", y="sum", data=df, estimator=np.median, ci=None, join=False, markers='d', scale=0.6, color='0.25')
plt.setp(ax.lines, zorder=100)
plt.setp(ax.collections, zorder=100)
plt.setp(ax.collections[-1], label='median')
ax.set(ylabel=r"$Sgo1_{peri-CEN}$ (min)")


add_stat_annotation(ax, data=df, x='strain', y='sum',
                    box_pairs=[('wt', 'glc7-12')],
                    test='Mann-Whitney', text_format='star', loc='outside', verbose=2)

plt.xticks(np.arange(0, 2, 1), ('GLC7', r'$\it{glc7-12}$'))

plt.yticks(np.arange(0, 12, step=1), ('0', '15', '30', '45', '60', '75', '90', '105', '120', '135', '150', '165'))

plt.xlabel('')
# plt.legend()
plt.show()

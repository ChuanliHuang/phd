import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statannot import add_stat_annotation


# sns.set(style='whitegrid')
file_name = '/Users/kikawaryoku/Desktop/data.xlsx'
df = pd.read_excel(file_name, sheet_name=2)
# fig, ax = plt.subplots(figsize=(16, 4.8))
ax = sns.swarmplot(x="type", y="distance", data=df, color='tab:red', size=2)
ax = sns.pointplot(x="type", y="distance", data=df, estimator=np.mean, ci=None, join=False, markers='d', scale=0.6, color='0.25')
plt.setp(ax.lines, zorder=100)
plt.setp(ax.collections, zorder=100)
plt.setp(ax.collections[-1], label='mean')
ax.set(ylabel=r'distance$_{interKT}$ ($\mu$m)')


add_stat_annotation(ax, data=df, x='type', y='distance',
                    box_pairs=[('wt_75', 'glc7_180')],
                    test='t-test_ind', text_format='star', loc='outside', verbose=2)

plt.xticks(np.arange(0, 2, 1), (r'GLC7$_{t75}$', r'$\it{glc7-12}_{t180}$'))

plt.xlabel('')
plt.legend()
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statannot import add_stat_annotation


# sns.set(style='whitegrid')
file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/NAA_PI_1_quantification/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
# fig, ax = plt.subplots(figsize=(16, 4.8))

ax = sns.boxplot(x="duration", y="condition", orient='h', data=df)
# ax = sns.pointplot(x="duration", y="condition", orient='h', data=df, estimator=np.median, ci=None, join=False, markers='d', scale=0.6, color='0.25')
plt.setp(ax.lines, zorder=100)
plt.setp(ax.collections, zorder=100)
# plt.setp(ax.collections[-1], label='median')
# ax.set(ylabel="Sgo1 as dot (mins)")
# add_stat_annotation(ax, data=df, x='condition', y='duration',
#                     box_pairs=[(1, 2), (1, 3), (1, 4), (3, 4)],
#                     test='Mann-Whitney', text_format='star', loc='outside', verbose=2)
#
# plt.xticks(np.arange(0, 4, 1), ('-\n\n''-', '-\n\n''+', '+\n\n''-', '+\n\n''+'))
#
# plt.yticks(np.arange(0, 80, step=10), ('0', '10', '20', '30', '40', '50', '60', '>60'))
#
# plt.xlabel('')
# # plt.legend()
plt.show()

# sns.set(style='whitegrid')
# file_name = '/Users/kikawaryoku/Desktop/fluo/fluo_intensity.xlsx'
# df = pd.read_excel(file_name, sheet_name=0)
# ax = sns.swarmplot(x="strain", y="g", data=df, size=4)
# ax = sns.pointplot(x="strain", y="g", data=df, estimator=np.median, ci=None, join=False, markers='d', scale=0.6, color='0.25')
# plt.setp(ax.lines, zorder=100)
# plt.setp(ax.collections, zorder=100)
# plt.setp(ax.collections[-1], label='median')
# ax.set(ylabel="Sgo1 intensity")
# add_stat_annotation(ax, data=df, x='strain', y='g',
#                     box_pairs=[("wt", "rts1d")],
#                     test='t-test_paired', text_format='star', loc='outside', verbose=2)
# plt.xticks(np.arange(0, 2, 1), ('wt', r'$\it{rts1\Delta}$'))
# # plt.yticks(np.arange(20, 100, step=10), ('20', '30', '40', '50', '60', '70', '80', '>80'))
# plt.xlabel('')
# plt.legend()
# plt.show()

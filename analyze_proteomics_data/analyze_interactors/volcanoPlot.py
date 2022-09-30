import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from adjustText import adjust_text

fold_change_cut = 4
p_value_cut = 4

# file_name = '/Users/kikawaryoku/Desktop/Sgo1 IP-MS rep2 DEP analysis/PE/results_PE.txt'
# df = pd.read_csv(file_name, sep='\t')
# texts = []
# for i, row in df.iterrows():
#     x = row['X23137_WT_PE__vs_X1176_notag_PE__ratio']
#     y = row['X23137_WT_PE__vs_X1176_notag_PE__p.val']
#     y = math.log10(y) * -1
#     if abs(x) > fold_change_cut and y > p_value_cut:
#         plt.plot(x, y, '.', color='royalblue', markersize=2)
#         texts.append(plt.text(x, y, row['name'], fontsize=3))
#     else:
#         plt.plot(x, y, '.', color='lightsteelblue', markersize=2)



file_name = '/Users/kikawaryoku/Downloads/results.txt'
df = pd.read_csv(file_name, sep='\t')
texts = []
for i, row in df.iterrows():
    x = row['X23137_WT_FT__vs_X29443_Bub1.DK_FT__ratio']
    y = row['X23137_WT_FT__vs_X29443_Bub1.DK_FT__p.val']
    y = math.log10(y) * -1
    if row['name'] == 'SGO1' or row['name'] == 'TPD3' or row['name'] == 'PPH21' or row['name'] == 'PPH22':
        plt.plot(x, y, '.', color='red', markersize=2)
        texts.append(plt.text(x, y, row['name'], fontsize=3))
    elif abs(x) > fold_change_cut and y > p_value_cut:
        plt.plot(x, y, '.', color='royalblue', markersize=2)
        texts.append(plt.text(x, y, row['name'], fontsize=3))
    else:
        plt.plot(x, y, '.', color='lightsteelblue', markersize=2)


x_cut = np.arange(-10, 10, 0.1)
p_cut = [p_value_cut] * len(x_cut)
y_cut = np.arange(0, 14, 0.1)
f_cut_1 = [fold_change_cut] * len(y_cut)
f_cut_2 = [-fold_change_cut] * len(y_cut)
# plt.text(-4, 18, 'noTag', fontsize=10, color='tab:orange')
plt.text(-6, 18, r'bub1$_{\Delta kinase}$', fontsize=10, color='tab:orange')
plt.text(4, 18, r'WT', fontsize=10, color='tab:orange')
# plt.text(6, 23, r'Rts1$\Delta$', fontsize=10, color='tab:orange')
# plt.plot(x_cut, p_cut, '--', color='grey')
# plt.plot(f_cut_1, y_cut, '--', color='grey')
# plt.plot(f_cut_2, y_cut, '--', color='grey')
# plt.xlim(-6.5, 6.5)
# plt.ylim(-0.5, 20.5)
plt.xlabel(r'log$_2$ fold change')
plt.ylabel(r'-log$_{10}$ P')
adjust_text(texts, only_move={'points':'y', 'texts':'y'})
plt.show()
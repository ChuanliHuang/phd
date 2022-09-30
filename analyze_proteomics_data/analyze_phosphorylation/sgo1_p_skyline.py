import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

file_name = '/Users/kikawaryoku/Desktop/Bessie_rep2.xlsx'
df = pd.read_excel(file_name, engine='openpyxl', sheet_name=0)
norm_factor = df.iloc[1][1:]
p_colors = ['tab:blue', 'tab:orange', 'tab:green']
strain_id = 2
intensities = df.iloc[strain_id][1:] / norm_factor
peptides = intensities.index.tolist()
fold_changes = np.log2(intensities.tolist())
for i in range(len(intensities)):
    peptide = peptides[i]
    fold_change = fold_changes[i]
    start = int(peptide[0:3])
    stop = int(peptide[4:7])
    p_num = int(peptide[-2]) - 1
    plt.plot([start, stop], [fold_change, fold_change], color=p_colors[p_num])
x = np.linspace(0, 590)
y = [0*i for i in x]
plt.plot(x, y, '--', color='grey')
blue_line = mlines.Line2D([], [], color='tab:blue', label='1')
orange_line = mlines.Line2D([], [], color='tab:orange', label='2')
green_line = mlines.Line2D([], [], color='tab:green', label='3')
plt.legend(handles=[blue_line, orange_line, green_line], title='phospho num')
plt.title('{}'.format(df.strain[strain_id]))
plt.ylabel('log$_2$ fold change to WT')
plt.xlabel('position within Sgo1')
plt.ylim(-8.5, 8.5)
plt.xlim(0, 590)
plt.show()
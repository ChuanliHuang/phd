import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = '/Users/kikawaryoku/OneDrive - University of Edinburgh/shugoshin/BS_Sgo1_IP-MS/Sgo1phosphosite_cleaned.xlsx'
df = pd.read_excel(file_name, sheet_name=0, engine='openpyxl')
all_positions = df['positions']
strains = ['Score C1(wt)', 'Score C2(wt)', 'Score C3(wt)', 'Score G1(3A)', 'Score G2(3A)', 'Score G3(3A)']
names = ['wt_rep_1', 'wt_rep_2', 'wt_rep_3', 'sgo1-3A_rep_1', 'sgo1-3A_rep_2', 'sgo1-3A_rep_3']

i = 0
for strain in strains:
    strain_positions = df[strain]
    selection = strain_positions.notna()
    x = all_positions[selection]
    y = [i] * len(x)
    plt.plot(x, y, '.')
    i += 1
plt.xlim(1, 591)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
plt.ylim(-0.5, 5.5)
plt.yticks(np.arange(6), names)
plt.show()


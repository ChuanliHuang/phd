import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_name = '/Users/kikawaryoku/OneDrive - University of Edinburgh/shugoshin/SG_Sgo1_IP-MS/SG_Sgo1_phospho-sites.xlsx'
df = pd.read_excel(file_name, sheet_name=0, engine='openpyxl')
all_positions = df['Positions.within.proteins']
strains = ['Score.wt_1', 'Score.wt_2', 'Score.wt_3']
names = ['wt rep1', 'wt rep2', 'wt rep3']

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
plt.ylim(-0.5, 2.5)
plt.yticks(np.arange(3), names)
plt.show()
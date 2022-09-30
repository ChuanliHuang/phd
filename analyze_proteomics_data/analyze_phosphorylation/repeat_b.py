import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = '/Users/kikawaryoku/Desktop/Sgo1 IP-MS repeat_b/Sgo1-phospho.xlsx'
df = pd.read_excel(file_name, sheet_name=0, engine='openpyxl')
all_positions = df['Positions within proteins']
strains = ['Score 1176_notag_ben_PE', 'Score 23137_WT_ben_PE', 'Score 29443_Bub1-DK_ben_PE', 'Score 29444_Rts1-D_ben_PE', 'Score 1176_notag_cyc_PE', 'Score 23137_WT_cyc_PE', 'Score 29443_Bub1-DK_cyc_PE', 'Score 29444_Rts1-D_cyc_PE']
names = ['ben notag', 'ben WT', 'ben Bub1ΔK', 'ben Rts1Δ', 'cyc notag', 'cyc WT', 'cyc Bub1ΔK', 'cyc Rts1Δ']

i = 0
for strain in strains:
    strain_positions = df[strain]
    selection = strain_positions.notna()
    x = all_positions[selection]
    y = [i] * len(x)
    plt.plot(x, y, 'o')
    i += 1
plt.xlim(1, 591)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
plt.ylim(-0.5, 7.5)
plt.yticks(np.arange(8), names)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_name = '/Users/kikawaryoku/Desktop/Sgo1 IP-MS repeat_b/Sgo1-phospho.xlsx'
df = pd.read_excel(file_name, sheet_name=0, engine='openpyxl')
all_positions = df['Positions within proteins']
strains = ['Score 1176_notag_ben_PE', 'Score 23137_WT_ben_PE', 'Score 29443_Bub1-DK_ben_PE', 'Score 29444_Rts1-D_ben_PE']

i = 0
for strain in strains:
    strain_positions = df[strain]
    selection = strain_positions.notna()
    x = all_positions[selection]
    y = [2*i] * len(x)
    plt.plot(x, y, '.')
    i += 1


file_name = '/Users/kikawaryoku/Desktop/Sgo1 IP-MS repeat_c/Sgo1-phospho.xlsx'
df = pd.read_excel(file_name, sheet_name=0, engine='openpyxl')
all_positions = df['Positions within proteins']
strains = ['Score ben_1176_notag_PE', 'Score ben_23137_WT_PE', 'Score ben_29443_Bub1-DK_PE', 'Score ben_29444_Rts1-D_PE']

names = ['ben notag rep1', 'ben notag rep2', 'ben WT rep1', 'ben WT rep2', 'ben Bub1ΔK rep1', 'ben Bub1ΔK rep2', 'ben Rts1Δ rep1', 'ben Rts1Δ rep2']

i = 0
for strain in strains:
    strain_positions = df[strain]
    selection = strain_positions.notna()
    x = all_positions[selection]
    y = [2 * i + 1] * len(x)
    plt.plot(x, y, '.')
    i += 1
plt.xlim(1, 591)
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=False)
plt.xlabel('position within Sgo1')
plt.ylim(-0.5, 7.5)
plt.yticks(np.arange(8), names)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = '/Users/kikawaryoku/OneDrive - University of Edinburgh/shugoshin/Sgo1_IP-MS/Sgo1 IP-MS repeat_c/Sgo1-phospho.xlsx'
df = pd.read_excel(file_name, engine='openpyxl', sheet_name=0)
x = df['Positions within proteins']
# names = ['Intensity 1176_notag_ben_PE', 'Intensity 23137_WT_ben_PE', 'Intensity 29443_Bub1-DK_ben_PE', 'Intensity 29444_Rts1-D_ben_PE']
names = ['Intensity ben_1176_notag_PE', 'Intensity ben_23137_WT_PE', 'Intensity ben_29443_Bub1-DK_PE', 'Intensity ben_29444_Rts1-D_PE']
for i in range(4):
    name = names[i]
    # LFQ_intensity = LFQ_intensities[i]
    # y = df[name] / LFQ_intensity
    y = np.divide(df[name], df['Intensity ben_23137_WT_PE'])
    # y = y.to_numpy()
    # y = np.log10(y)
    plt.plot(x, y, '.', label=name)

plt.legend()
# plt.xlim(140, 160)
# plt.xlim(400, 525)
plt.ylabel('fold change to WT')
plt.xlabel('position within Sgo1')
plt.show()
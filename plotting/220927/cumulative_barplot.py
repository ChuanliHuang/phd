import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import pandas as pd

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_ChIP_data_analysis/070922_pH2A ChIP-seq_00/data/Cen_vs_non-Cen_ratio.xlsx'
df = pd.read_excel(file_name, sheet_name=0, index_col=0)

totals = df.total.tolist()
cens = df.cens.tolist()
arms = df.arms.tolist()
cens_fraction = [str(round((cens[i]/totals[i]) * 100))+'%' for i in range(2)]
arms_fraction = [str(round((arms[i]/totals[i]) * 100))+'%' for i in range(2)]
labels = ['tension', 'no tension']

#
width = 0.5       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, cens, width, color='coral', bottom=arms, label='Centromeres')
ax.bar(labels, arms, width, color='tab:cyan', label='Chromosome arms')
ls = [cens_fraction, arms_fraction]
j = 0
for bars in ax.containers:
    ax.bar_label(bars, [ls[j][0], ls[j]][1], padding=-15)
    j += 1
ax.set_ylim(0, 1300000000)
ax.set_xticks([-0.6, 0, 1, 1.6])
ax.set_ylabel('sum calibrated RPM (million)')
ax.set_yticklabels(range(0, 1400, 200))
ax.legend()

plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
sns.set_theme(style="whitegrid")

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_ChIP_data_analysis/060422 Sgo1-6HA ChIP in hta1 mutants/summary.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
# df = df[df['repeat'] == 3]
g = sns.catplot(x="strain", y="%INPUT", ci='sd',
                hue="condition", col="loc",
                data=df, kind="bar",
                height=4, aspect=.7)
(g.set_axis_labels("")
  # .set_xticklabels(["SGO1\nHTA1", 'SGO1-6HA\nHTA1', 'SGO1-6HA\n'+r'$\it{hta1-S121A}$', 'SGO1-6HA\n'+r'$\it{hta1-S121D}$'], fontsize=5)
  .set_xticklabels(["no tag", 'wild type', 'H2A-S121A', 'H2A-S121D'], fontsize=7)
  # .set_xticklabels(["no tag", 'wild type', 'H2A-S121A'], fontsize=10)
  .set_titles('{col_name}')
  .legend.set_title(''))
plt.show()

# IMPORTANT -- to plot standard error, go to categorical.py and edit the 'sd' function
# ,ddof=1)/np.sqrt(len(stat_data))
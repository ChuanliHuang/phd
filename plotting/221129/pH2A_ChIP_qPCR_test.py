import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300

sns.set_theme(style="whitegrid")
file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_ChIP_data_analysis/150822_pH2A ChIP_00/analysis_2.xlsx'
df = pd.read_excel(file_name, sheet_name=1)

g = sns.catplot(
    data=df, x="region", y="%INPUT", row='strain', col="fix_time",
    kind="bar", height=4, aspect=.6,
)

(g.set_axis_labels("")
  # .set_xticklabels(["SGO1\nHTA1", 'SGO1-6HA\nHTA1', 'SGO1-6HA\n'+r'$\it{hta1-S121A}$', 'SGO1-6HA\n'+r'$\it{hta1-S121D}$'], fontsize=5)
  .set_xticklabels(["CEN4a", 'CEN4b', 'ARM4', 'peri-CEN4'], fontsize=7)
  # .set_xticklabels(["no tag", 'wild type', 'H2A-S121A'], fontsize=10)
  .set_titles('')
  # .legend.set_title('')
 )

plt.show()
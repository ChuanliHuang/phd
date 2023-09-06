import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np
import seaborn as sns

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/211105_Sgo1-EGFP_glc7-12_34C_quantification/data.xlsx'
df = pd.read_excel(file_name, sheet_name=1)
wt_df = df[df['strain'] == 'wt']
glc7_12_df = df[df['strain'] == 'glc7-12']

# wt_average = [wt_df[i].sum()/wt_df[i].count() for i in range(30, 195, 15)]
wt_median = [wt_df[i].median() for i in range(30, 195, 15)]
# glc7_12_average = [glc7_12_df[i].sum()/glc7_12_df[i].count() for i in range(30, 195, 15)]
glc7_12_median = [glc7_12_df[i].median() for i in range(30, 195, 15)]
#
# for i, row in wt_df.iterrows():
#     plt.plot(row[3:], 'lightsteelblue', linewidth=0.2)
#
# for i, row in glc7_12_df.iterrows():
#     plt.plot(row[3:], 'bisque', linewidth=0.2)


for i, row in wt_df.iterrows():
    plt.plot(range(30, 195, 15), row[3:], '.', color='tab:blue', alpha=0.3)

for i, row in glc7_12_df.iterrows():
    plt.plot(range(30, 195, 15), row[3:], '.', color='tab:orange', alpha=0.3)

plt.plot(np.arange(30, 195, 15), wt_median, linewidth=2, label=r'wild type', color='tab:blue')
plt.plot(np.arange(30, 195, 15), glc7_12_median, linewidth=2, label=r'$\it{glc7-12}$', color='tab:orange')
plt.xticks(np.arange(30, 195, step=15), ('30', '45', '60', '75', '90', '105', '120', '135', '150', '165', '180'))
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylim(-0.05, 2.55)
# degree_sign = u'\N{DEGREE SIGN}'
# plt.title('34'+degree_sign+'C')
plt.legend()
plt.show()
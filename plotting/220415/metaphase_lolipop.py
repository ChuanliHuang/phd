import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/3_ChIP_data_analysis/060422 Sgo1-6HA ChIP in hta1 mutants/check/spindle_count.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

plt.stem(df['meta'][0:4], basefmt='none')
my_range = range(0, 4)
# plt.xticks(my_range, ["SGO1\nHTA1", 'SGO1-6HA\nHTA1', 'SGO1-6HA\n'+r'$\it{hta1-S121A}$', 'SGO1-6HA\n'+r'$\it{hta1-S121D}$'])
plt.xticks(my_range, ["no tag", 'wild type', 'H2A-S121A', 'H2A-S121D'])
plt.ylabel('%Cells with metaphase spindle')
plt.yticks(np.arange(0, 120, step=20), ('0%', '20%', '40%', '60%', '80%', '100%'))
# plt.xlim(-1, 4)
plt.show()
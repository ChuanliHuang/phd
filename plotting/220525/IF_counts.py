import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import pandas as pd
import numpy as np


file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_westerns/250522_pH2A_timecourse_repeat_b/spindle count/tubulin IF.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
# plt.plot(df.time, df.others, '-o', label='others')
plt.plot(df.time, df.meta, '-o', label='metaphase spindle')
plt.plot(df.time, df.ana, '-o', label='anaphase spindle')
xticks = np.arange(0, 195, 15)
plt.xticks(xticks)
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel('% Cells')
# plt.yticks(np.arange(0, 120, step=20), ('0%', '20%', '40%', '60%', '80%', '100%'))
plt.ylim (-5, 105)
plt.legend()
plt.show()


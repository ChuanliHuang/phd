import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


file_name = '/Users/kikawaryoku/Desktop/150422_pH2A_timecourse/tubulin IF.xlsx'
df = pd.read_excel(file_name, sheet_name=1)
plt.plot(df.time, df.others, '-o', label='others')
plt.plot(df.time, df.meta, '-o', label='metaphase')
plt.plot(df.time, df.ana, '-o', label='anaphase')
xticks = np.arange(0, 195, 15)
plt.xticks(xticks)
plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.ylabel('%cells')
plt.legend()
plt.show()
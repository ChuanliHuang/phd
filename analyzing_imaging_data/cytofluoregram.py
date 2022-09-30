import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = '/Users/kikawaryoku/Desktop/CH_Exp16b/co_loc_q/coloc_quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=1, header=None)
for i in range(0, 2):
    plt.plot(df.iloc[:, i], marker='o', markersize=2)
plt.ylim(-0.2, 1.05)
plt.ylabel('SRCC')
x = np.arange(0, 25, 5)
x_label = 2 * x
plt.xticks(x, x_label)
plt.xlabel('time (min)')
plt.show()
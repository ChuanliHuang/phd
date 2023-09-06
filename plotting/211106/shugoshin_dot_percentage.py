import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/211105_Sgo1-EGFP_glc7-12_34C_quantification/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_df = df[df['strain'] == 'wt']
glc7_12_df = df[df['strain'] == 'glc7-12']

wt = [wt_df[i].sum()/wt_df[i].count() for i in range(30, 195, 15)]
glc7_12 = [glc7_12_df[i].sum()/glc7_12_df[i].count() for i in range(30, 195, 15)]

plt.plot(wt, '-o', label='wild type')
plt.plot(glc7_12, '-o', label=r'$\it{glc7-12}$')
plt.xticks(np.arange(0, 11, step=1), ('30', '45', '60', '75', '90', '105', '120', '135', '150', '165', '180'))
plt.yticks(np.arange(0, 1.2, step=0.2), ('0', '20', '40', '60', '80', '100'))
# plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'% Cells with Sgo1-EGFP dot(s)')
# degree_sign = u'\N{DEGREE SIGN}'
# plt.title('34'+degree_sign+'C')
plt.legend()
plt.show()
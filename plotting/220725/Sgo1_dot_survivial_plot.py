from lifelines import KaplanMeierFitter
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220722_Bub1-3V5-AID_glc7-12/quantification.xlsx'
names = ['- NAA', '+NAA']


df = pd.read_excel(file_name, sheet_name=0)
for i in [0, 1]:
    selection = df['condition'] == i + 1
    T = df[selection]['duration']
    E = []
    for t in T:
        if t == 60:
            e = 0
        else:
            e = 1
        E.append(e)
    kmf = KaplanMeierFitter()
    kmf.fit(T, E)
    kmf.survival_function_
    kmf.plot_survival_function(label=names[i])

plt.yticks(np.arange(0, 1.2, step=0.2), ('0%', '20%', '40%', '60%', '80%', '100%'))
plt.xlabel(r'time after drug addition (min)')
plt.ylabel(r'% Cells with Sgo1-EGFP dot(s)')
plt.show()
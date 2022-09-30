from lifelines import KaplanMeierFitter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/NAA_PI_1_quantification/data.xlsx'
# names = ['-NAA -PIs', '-NAA +PIs', '+NAA -PIs', '+NAA +PIs']
names = ['- NAA', '-NAA +PIs', '+NAA', '+NAA +PIs']

# df = pd.read_excel(file_name, sheet_name=1)
# for i in range(len(df['condition'].unique())):
#     selection = df['condition'] == i+1
#     T = df[selection]['duration']
#     E = []
#     for t in T:
#         if t == 70:
#             e = 0
#         else:
#             e = 1
#         E.append(e)
#     kmf = KaplanMeierFitter()
#     kmf.fit(T, E)
#     kmf.survival_function_
#     kmf.plot_survival_function(label=names[i])

df = pd.read_excel(file_name, sheet_name=1)
for i in [0, 2]:
    selection = df['condition'] == i+1
    T = df[selection]['duration']
    T[T > 60] = 60
    print(T)
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

# plt.xticks(np.arange(0, 80, step=10), ('0', '10', '20', '30', '40', '50', '60', '>60'))
plt.yticks(np.arange(0, 1.2, step=0.2), ('0%', '20%', '40%', '60%', '80%', '100%'))
plt.xlabel(r'time after drug addition (min)')
plt.ylabel(r'% Cells with Sgo1-EGFP dot(s)')
plt.show()
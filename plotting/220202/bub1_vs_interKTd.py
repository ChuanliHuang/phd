import pandas as pd
import matplotlib.pyplot as plt

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/220124_Bub1-mNG_Mtw1-td/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

for cell in df['cell'].unique():
    selection = df['cell'] == cell
    g_int = df[selection]['g_intensity']
    r_distance = df[selection]['r_distance']
    selected_index = []
    for i in range(len(g_int)):
        if r_distance.values[i] > 0:
            selected_index.append(i)
    selected_index.append(int(selected_index[0]) - 1)
    r_distance = r_distance.values[selected_index]
    g_int = g_int.values[selected_index]

    plt.plot(r_distance, g_int, '.', color='tab:blue', alpha=0.3)
plt.xlim(-0.05, 2.15)
# plt.ylim(-100.5, 200.5)
plt.xlabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylabel('GFP intensity (a.u.)')
plt.show()
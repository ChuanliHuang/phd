import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/1_Image analysis/220124_Bub1-mNG_Mtw1-td/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

for cell in df['cell'].unique():
    selection = df['cell'] == cell
    time = (df[selection]['time'] - 1) * 10 + 20
    r_distance = df[selection]['r_distance']
    plt.plot(time, r_distance, '.', color='magenta', alpha=0.3)
x = []
y = []
for time in df['time'].unique():
    selection = df['time'] == time
    x.append((time - 1) * 10 + 20)
    g_int_median = df[selection]['r_distance'].median()
    y.append(g_int_median)
plt.plot(x, y, color='magenta', linewidth=2)

plt.xlabel(r'time after G1 release (min)')
plt.ylabel(r'distance$_{interKT}$ ($\mu$m)')
plt.ylim(-0.05, 2.55)
plt.show()
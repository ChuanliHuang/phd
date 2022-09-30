import pandas as pd
import matplotlib.pyplot as plt

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/220208_Bub1-mNG_Mtw1-td_noc/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

for cell in df['cell'].unique():
    selection = df['cell'] == cell
    time = (df[selection]['time'] - 1) * 10 + 20
    g_int = df[selection]['g_intensity']
    plt.plot(time, g_int, '.', color='lightgreen', alpha=0.3)
x = []
y = []
for time in df['time'].unique():
    selection = df['time'] == time
    x.append((time - 1) * 10 + 20)
    g_int_median = df[selection]['g_intensity'].median()
    y.append(g_int_median)
plt.plot(x, y, color='tab:green', linewidth=2, label='median')
plt.legend()
plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.ylabel('GFP intensity (a.u.)')
plt.ylim(-100,400)
plt.show()
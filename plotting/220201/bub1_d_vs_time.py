import pandas as pd
import matplotlib.pyplot as plt

file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/220126_Bub1 vs peri-CEN boarder/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

for cell in range(len(df['cell'].unique())):
    selection = (df['cell'] == cell) & (df['l'] == 0)
    distances = df[selection]['distance']
    time = (df[selection]['time'] - 1) * 10 + 20
    plt.plot(time, distances, '.', color='lightgreen', alpha=0.3)

x = []
y = []
for time in df['time'].unique():
    selection = (df['time'] == time) & (df['l'] == 0)
    x.append((time - 1) * 10 + 20)
    d_median = df[selection]['distance'].median()
    y.append(d_median)
plt.plot(x, y, color='tab:green', linewidth=2, label='median')
plt.legend()
plt.xlabel(r'time after $\alpha$ factor washout (min)')
plt.ylabel(r'distance$_{interBub1}$ ($\mu$m)')
plt.xlim(19.5, 150.5)
plt.show()
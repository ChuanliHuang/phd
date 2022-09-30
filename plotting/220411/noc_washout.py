import pandas as pd
import matplotlib.pyplot as plt


file_name = '/Users/kikawaryoku/Desktop/data.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt = df[df['strain'] == 'wt'].groupby(['frame']).sum()

fractions = []
for i, row in wt.iterrows():
    fraction = row['2_dot'] / (row['1_dot'] + row['2_dot'])
    fractions.append(fraction)

time = [(x+1)*15 for x in range(9)]
plt.plot(time, fractions, label='wt')

for strain_name in df['strain'].unique():
    if strain_name != 'wt':
        strain_df = df[df['strain'] == strain_name]
        fractions = []
        for i, row in strain_df.iterrows():
            fraction = row['2_dot'] / (row['1_dot'] + row['2_dot'])
            fractions.append(fraction)
        plt.plot(time, fractions, label=strain_name)

plt.legend()
plt.xlim(-0.5, 150.5)
plt.ylim(-0.05, 1.05)
plt.xlabel('time ater noc washout (min)')
plt.ylabel('fraction of cells with 2 CEN4 dots')
plt.show()
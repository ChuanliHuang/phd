import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/220126_Bub1 vs peri-CEN boarder/quantification.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
df_1 = df.copy()


for cell in range(len(df['cell'].unique())):
    for time in range(len(df['time'].unique())):
        selection1 = df[(df['cell']==cell+1)&(df['time']==time+1)&(df['l']==1)]['distance']
        selection2 = df[(df['cell']==cell+1)&(df['time']==time+1)&(df['l']==2)]['distance']
        l1 = selection1.values[0]
        l2 = selection2.values[0]
        row1 = selection1.index[0]
        row2 = selection2.index[0]
        if l1 > l2:
            df_1.iloc[row1, 3] = l2
            df_1.iloc[row2, 3] = l1

# plot interKT > 0
# df = df_1
# for i in range(len(df['cell'].unique())):
#     bub1_d = df[(df['cell'] == i+1)&(df['l'] == 0)]['distance']
#     l1 = df[(df['cell'] == i+1)&(df['l'] == 1)]['distance']
#     l2 = df[(df['cell'] == i+1)&(df['l'] == 2)]['distance']
#     plt.plot(bub1_d[list(bub1_d != 0)], l1[list(bub1_d != 0)], '.', color='tab:blue')
#     plt.plot(bub1_d[list(bub1_d != 0)], l2[list(bub1_d != 0)], '.', color='tab:orange')
#
# plt.ylim(-0.05, 1.305)
# plt.xlabel(r'interKT ($\mu$m)')
# plt.ylabel(r'Bub1 vs periCEN border distance ($\mu$m)')
# plt.show()

# plot interKT = 0
df = df_1
res = []
for i in range(len(df['cell'].unique())):
    bub1_d = df[(df['cell'] == i+1)&(df['l'] == 0)]['distance']
    l1 = df[(df['cell'] == i+1)&(df['l'] == 1)]['distance']
    l2 = df[(df['cell'] == i+1)&(df['l'] == 2)]['distance']
    for j in l1[list(bub1_d == 0)]:
        res.append(j)
ax = sns.swarmplot([0]*len(res), res, color='tab:green')
plt.xlim(-0.1, 0.1)
plt.ylim(-0.05, 1.305)
plt.xlabel(r'interKT=0 ($\mu$m)')
plt.xticks([])
plt.ylabel(r'Bub1 vs periCEN border distance ($\mu$m)')
plt.show()
import pandas as pd
import math
import matplotlib.pyplot as plt
df = pd.read_excel('/Users/kikawaryoku/Desktop/k_dis_vs_s_int/res.xlsx')
selection = df['cell_id']
data = df[selection == 1]
k_dis_ls = []
for i, row in data.iterrows():
    k_dis = math.sqrt((row.r1_x - row.r2_x) ** 2 + (row.r1_y - row.r2_y) ** 2)
    k_dis_ls.append(k_dis)
s_int_ls = data.g_int.tolist()
fig, ax = plt.subplots()
ax.plot(k_dis_ls, 'r', marker='.')
ax.set_xlabel('frame')
ax.set_ylabel('k_dis', color='red')
ax1 = ax.twinx()
ax1.plot(s_int_ls, 'g', marker='.')
ax1.set_ylabel('s_int', color='green')
plt.title('kinetochore distance vs Sgo1 intensity')
plt.show()

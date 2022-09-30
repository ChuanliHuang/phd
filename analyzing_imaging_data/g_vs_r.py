import pandas as pd
import matplotlib.pyplot as plt

file_name ='/Users/kikawaryoku/Desktop/fluo/fluo_intensity.xlsx'
df = pd.read_excel(file_name, sheet_name=0)
wt_g = []
wt_r = []
rts1d_g = []
rts1d_r = []
for i, row in df.iterrows():
    if row.strain == 'wt':
        wt_g.append(row.g)
        wt_r.append(row.r)
    elif row.strain == 'rts1d':
        rts1d_g.append(row.g)
        rts1d_r.append(row.r)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(wt_r, wt_g, 'o', fillstyle='none', color='grey', label='wt')
ax.plot(rts1d_r, rts1d_g, 'x', color='black', label=r'$rts1\Delta$')
ax.set_xlabel('Mtw1 intensity')
ax.xaxis.label.set_color('tab:red')
ax.set_ylabel('Sgo1 intensity')
ax.yaxis.label.set_color('tab:green')
ax.spines['bottom'].set_color('tab:red')
ax.tick_params(axis='x', colors='tab:red')
ax.spines['left'].set_color('tab:green')
ax.tick_params(axis='y', colors='tab:green')
plt.legend()
plt.show()
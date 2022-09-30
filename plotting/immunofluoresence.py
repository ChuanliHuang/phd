import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/kikawaryoku/Desktop/CH_exp14a_IF.xlsx', sheet_name=2)
df = df.astype('float64')
for i, row in df.iterrows():
    row.other /= row.total / 100
    row.meta /= row.total / 100
    row.ana /= row.total / 100

plt.plot(df.time, df.other, marker='o', label='other')
plt.plot(df.time, df.meta, marker='o', label='metaphase')
plt.plot(df.time, df.ana, marker='o', label='anaphase')
plt.xlabel('time (min)')
plt.ylabel('%')
plt.title('met-cdc20 met-scc1 in -met')
plt.legend()
plt.show()
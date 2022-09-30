import pandas as pd
import matplotlib.pyplot as plt

file_name = '/Users/kikawaryoku/OneDrive - University of Edinburgh/shugoshin/proteomics/Sgo1phosphosite_cleaned.xlsx'
df = pd.read_excel(file_name)
dfa = df.copy()
positions = dfa.positions

dfa = dfa.notna()
dfa = dfa.astype(int)


sgo1_wt = []
sgo1_3a = []

for i, row in dfa.iterrows():
    detection_number_wt = row['Score C1(wt)'] + row['Score C2(wt)'] + row['Score C3(wt)']
    sgo1_wt.append(detection_number_wt)
    detection_number_3a = row['Score G1(3A)'] + row['Score G2(3A)'] + row['Score G3(3A)']
    sgo1_3a.append(detection_number_3a)

diffs = []
for j in range(len(sgo1_3a)):
    diff = sgo1_3a[j] - sgo1_wt[j]
    diffs.append(diff)

plt.plot(positions, diffs, 'o')
plt.show()
import pandas as pd
import numpy as np
import csv



file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/211105_Sgo1-EGFP_glc7-12_34C_quantification/data.xlsx'
df_sgo1 = pd.read_excel(file_name, sheet_name=0)
df_dkt = pd.read_excel(file_name, sheet_name=1)

wt_df_sgo1 = df_sgo1[df_sgo1['strain'] == 'wt']
wt_df_dkt = df_dkt[df_dkt['strain'] == 'wt']
glc7_df_dkt = df_dkt[df_dkt['strain'] == 'glc7-12']

wt_df_sgo1_dot = wt_df_sgo1[wt_df_sgo1['sum'] != 0]
wt_df_dkt_dot = wt_df_dkt[wt_df_sgo1['sum'] != 0]

last_sgo1_dot_position = []
for i, row in wt_df_sgo1_dot.iterrows():
    row = row[3:-1]
    one_positions = np.where(row == 1)
    last_sgo1_dot_position.append(one_positions[0][-1])
# print(last_sgo1_dot_position)

removal_ds = []
j = 0
for i, row in wt_df_dkt_dot.iterrows():
    row = list(row[3:])
    index_d_removal = last_sgo1_dot_position[j] + 1
    if index_d_removal <= 10:
        removal_ds.append(row[index_d_removal])
    j += 1
# removal_ds = np.array(removal_ds, dtype=float)

glc7_max = []
for i, row in glc7_df_dkt.iterrows():
    row = list(row[3:])
    if max(row) < 3:
        glc7_max.append(max(row))
# glc7_max = np.array(glc7_max, dtype=float)


file_name = '/Users/kikawaryoku/Desktop/removal_vs_max.csv'
with open(file_name, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(removal_ds)
        writer.writerow(glc7_max)

# have to transpose in excel mannually
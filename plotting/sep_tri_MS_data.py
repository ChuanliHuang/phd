import pandas as pd

file_name = '/Users/kikawaryoku/Desktop/Sgo1_IP-MS_analysis/proteinGroups_CHuang_FT_LFQ_iBAQ.xlsx'
df = pd.read_excel(file_name, sheet_name=1)
col_name_arr = df.columns.values
col_name_ser = pd.Series(col_name_arr)
selection = col_name_ser.str.contains('Rep1')
print(selection)
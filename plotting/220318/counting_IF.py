import matplotlib.pyplot as plt
import pandas as pd


file_name = '/Users/kikawaryoku/Library/CloudStorage/OneDrive-UniversityofEdinburgh/shugoshin/0_Image analysis/220318_tubulin IF_ pH2A/data/raw.xlsx'
df = pd.read_excel(file_name, sheet_name=0)

# Reorder it following the values:
my_range = range(0, len(df.index))

# Make the plot
plt.stem(df['percentage'] * 100, basefmt='none')
plt.xticks(my_range, [r'$bub1_{\Delta kinase}$', 'SGO1-EGFP \n MTW1-tdTomato', 'wildtype'])
# plt.gca().set_yticklabels([f'{x:.0%}' for x in plt.gca().get_yticks()])
plt.xlim(-1, 3)
plt.ylabel('% cells with metaphase spindle')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_name = '/Users/kikawaryoku/Desktop/data.xlsx'
df = pd.read_excel(file_name)
strain_nums = [9233, 21821, 21824, 24855]
strains = ['WT', 'SILK + RxVxF', 'SILK', 'RxVxF']
colors = ['r', 'g', 'b', 'y']
sns.set_color_codes()
def give_data(strain):
    strain = strain
    strain_df = df[(df['strain'] == strain) & (df['1st_cycle_sgo_ex_frames'].notna())]
    data = strain_df['1st_cycle_sgo_ex_frames'].astype(int)
    return data

fig, axes = plt.subplots(2, 2)
plt.delaxes(axes[1, 1])
for i, ax in enumerate(fig.axes):
    strain_num = strain_nums[i]
    strain = strains[i]
    color = colors[i]
    data = give_data(strain)
    sns.distplot(data, color=color, ax=ax)
    ax.set_title('{} (cell number = {})'.format(strain, len(data)))
    ax.set_xlabel('Sgo1 dot lasting frames')
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 0.4)
    ax.set_ylabel('frequency')
plt.setp(axes)
plt.tight_layout()
plt.show()
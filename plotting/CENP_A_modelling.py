import random
import numpy as np
import pandas as pd
# 0 = H3; 1 = CENP_A
class Cell():
    'A strand of DNA with nucleosomes'
    def __init__(self, cell_id, generation, parent, nucleosome_composition):
        self.cell_id = cell_id
        self.generation = generation
        self.parent = parent
        self.nucleosome_composition = nucleosome_composition
    def make_df_entry(self):
        a = np.array(self.nucleosome_composition)
        d = {'cell_id': self.cell_id, 'generation': self.generation, 'parent': self.parent, 'nuc_comp': [a]}
        df_entry = pd.DataFrame(data=d)
        return df_entry

def init_cell_0(nucleosome_num, CENP_A_fraction):
    nucleosome_composition = [0] * nucleosome_num
    for i in range(nucleosome_num):
        if random.random() < CENP_A_fraction:
            nucleosome_composition[i] = 1
    cell = Cell(0, 0, 0, nucleosome_composition)
    return cell


nucleosome_num = 10
CENP_A_fraction = 1
cell_0 = init_cell_0(nucleosome_num, CENP_A_fraction)
df = cell_0.make_df_entry()
print(df)


import numpy as np
import pandas as pd
import random


def init_cell_0(nucleosome_num, CENP_A_fraction):
    """initiate cell 0"""
    global data
    cell_0_nuc_comp = np.zeros(nucleosome_num, dtype=int)
    for i in range(nucleosome_num):
        if random.random() < CENP_A_fraction:
            cell_0_nuc_comp[i] = 1
    cell_0 = np.array((0, 0, cell_0_nuc_comp), dtype=dt)
    data = np.append(data, [cell_0], axis=0)


def replenish_cenp_a(mother):
    """replenishment that happens in a positional-based method"""
    cenp_a_positions = np.argwhere(mother['nucleosome_composition'] == 1).flatten()
    mu, sigma = 0, 1  # mean and standard deviation
    for i in cenp_a_positions:
        # generate a random integer from a normal distribution as the distance of deposition
        rn = np.random.normal(mu, sigma)
        distance_of_deposition = round(rn)
        # deposit
        new_cenp_a_position = i + distance_of_deposition
        if new_cenp_a_position in range(nucleosome_num):
            mother['nucleosome_composition'][new_cenp_a_position] = 1
    return mother


def dilute_cenp_a(mother):
    """CENP-A from mother strand distributed to daughter strands"""
    dgt_1_nuc_comp = np.zeros(nucleosome_num, dtype=int)
    dgt_2_nuc_comp = np.zeros(nucleosome_num, dtype=int)
    for i in range(nucleosome_num):
        if mother['nucleosome_composition'][i] == 1:
            if random.random() < dist_bias:
                dgt_1_nuc_comp[i] = 1
            else:
                dgt_2_nuc_comp[i] = 1
    return dgt_1_nuc_comp, dgt_2_nuc_comp


def replicate_a_cell(cell_id):
    """replicate a selected cell"""
    global data
    mother = data[cell_id].copy()
    dgt_generation = mother['generation'] + 1
    dgt_parent = cell_id

    # replenishment
    for i in range(replenish_rounds):
        mother = replenish_cenp_a(mother)
    # dilution
    dgt_1_nuc_comp, dgt_2_nuc_comp = dilute_cenp_a(mother)

    dgt1 = np.array((dgt_generation, dgt_parent, dgt_1_nuc_comp), dtype=dt)
    dgt2 = np.array((dgt_generation, dgt_parent, dgt_2_nuc_comp), dtype=dt)
    data = np.append(data, [dgt1], axis=0)
    data = np.append(data, [dgt2], axis=0)


def start():
    """start simulation"""
    init_cell_0(nucleosome_num, cenp_a_fraction)
    gen_end = 2 ** generations_to_simulate - 1
    for i in range(gen_end):
        replicate_a_cell(i)


# configurations
nucleosome_num = 10
cenp_a_fraction = 0.04
dist_bias = 0.5
generations_to_simulate = 4
replenish_rounds = 1
dt = np.dtype([('generation', np.int32), ('parent', np.int32),
               ('nucleosome_composition', np.int32, (nucleosome_num,))])  # defining data type of structured arrays
data = np.array([], dtype=dt)  # an array to store structured arrays

start()

df = pd.DataFrame({'generation': data['generation'], 'parent': data['parent'],
                   'nucleosome_composition': data['nucleosome_composition'].tolist()})
df.index.name = 'cell_id'

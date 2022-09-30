import random
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import configurations
from configurations import dt


def enter_a_cell(cell):
    """only enter cell with reasonable CENP-A density"""
    global data
    cenp_a_density = cell['nucleosome_composition'].sum() / configurations.nucleosome_num
    up_lim = (1 + configurations.density_max_variation) * configurations.cenp_a_fraction
    low_lim = (1 - configurations.density_max_variation) * configurations.cenp_a_fraction
    if low_lim < cenp_a_density < up_lim:
        data = np.append(data, [cell], axis=0)


def init_cell_0(nucleosome_num, CENP_A_fraction):
    """initiate a certain number of cell 0"""
    global data
    cell_0_nuc_comp = np.zeros(nucleosome_num, dtype=int)
    for i in range(nucleosome_num):
        if random.random() < CENP_A_fraction:
            cell_0_nuc_comp[i] = 1
    cell_0 = np.array((0, 0, cell_0_nuc_comp), dtype=dt)
    enter_a_cell(cell_0)


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
        if new_cenp_a_position in range(configurations.nucleosome_num):
            if random.random() < configurations.amplitude_factor:
                mother['nucleosome_composition'][new_cenp_a_position] = 1
    return mother


def dilute_cenp_a(mother):
    """CENP-A from mother strand distributed to daughter strands"""
    dgt_1_nuc_comp = np.zeros(configurations.nucleosome_num, dtype=int)
    dgt_2_nuc_comp = np.zeros(configurations.nucleosome_num, dtype=int)
    for i in range(configurations.nucleosome_num):
        if mother['nucleosome_composition'][i] == 1:
            if random.random() < configurations.dist_bias:
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
    for i in range(configurations.replenish_rounds):
        mother = replenish_cenp_a(mother)
    # dilution
    dgt_1_nuc_comp, dgt_2_nuc_comp = dilute_cenp_a(mother)

    dgt1 = np.array((dgt_generation, dgt_parent, dgt_1_nuc_comp), dtype=dt)
    dgt2 = np.array((dgt_generation, dgt_parent, dgt_2_nuc_comp), dtype=dt)
    enter_a_cell(dgt1)
    enter_a_cell(dgt2)


def start():
    """start simulation"""
    for i in range(configurations.initiate_cell_number):
        init_cell_0(configurations.nucleosome_num, configurations.cenp_a_fraction)
    j = 0
    try:
        while data[j]['generation'] < configurations.generations_to_simulate:
            replicate_a_cell(j)
            j += 1
    except IndexError:
        return

def show_APEX_plot():
    plt.imshow(data['nucleosome_composition'], cmap='gray')
    plt.title('AF={} RR={} MV={}'.format(configurations.amplitude_factor, configurations.replenish_rounds,
                                         configurations.density_max_variation))
    plt.ylabel('cell id')
    plt.xlabel('nucleosome position')
    white_patch = mpatches.Patch(color='white', label='CENP-A')
    black_patch = mpatches.Patch(color='black', label='H3')
    plt.legend(handles=[white_patch, black_patch])
    plt.show()


def show_cenp_a_density():
    sns.set(style="whitegrid")
    density_ls = []
    generation_ls = data['generation'].tolist()
    for i in range(len(data)):
        density = data['nucleosome_composition'][i].sum() / configurations.nucleosome_num
        density_ls.append(density)
    d = {'generation': generation_ls, 'CENP-A density': density_ls}
    df = pd.DataFrame(d)
    ax = sns.swarmplot(x="generation", y="CENP-A density", data=df)
    plt.title('AF={} RR={} MV={}'.format(configurations.amplitude_factor, configurations.replenish_rounds,
                                         configurations.density_max_variation))
    plt.show()


def save_data():
    file_name = '.xlsx'
    df = pd.DataFrame({'generation': data['generation'], 'parent': data['parent'],
                       'nucleosome_composition': data['nucleosome_composition'].tolist()})
    df.index.name = 'cell_id'
    df.to_excel(file_name)


if __name__ == '__main__':
    start()
    show_APEX_plot()

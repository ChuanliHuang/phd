import numpy as np
# configurations
nucleosome_num = 2500
cenp_a_fraction = 0.04
dist_bias = 0.5
generations_to_simulate = 20
replenish_rounds = 3
amplitude_factor = 0.7
initiate_cell_number = 100
density_max_variation = 0.1
dt = np.dtype([('generation', np.int32), ('parent', np.int32),
               ('nucleosome_composition', np.int32, (nucleosome_num,))])  # defining data type of structured arrays
data = np.array([], dtype=dt)  # an array to store structured arrays

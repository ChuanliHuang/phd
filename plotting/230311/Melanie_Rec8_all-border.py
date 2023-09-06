import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300
import numpy as np


def pile_up(_df):
    _means = _df.mean(axis=1, skipna=True)
    _stds = _df.std(axis=1, skipna=True)
    _cis = 1.96 * _stds / np.sqrt(16)
    _means = _means.values.tolist()
    _cis = _cis.values.tolist()
    _lower = [_means[i] - _cis[i] for i in range(len(_means))]
    _upper = [_means[i] + _cis[i] for i in range(len(_means))]
    return _means, _lower, _upper


def select_region(x, y, _size):
    x_selected = []
    y_selected = []

    for i in range(len(x)):
        if -_size <= x[i] <= _size:
            x_selected.append(x[i])
            y_selected.append(y[i])
    return y_selected

file_name = '/Users/kikawaryoku/Desktop/Melanie2023_Rec8ChIP-seq_r1/rec8-14d_border.xlsx'
wt_df = pd.read_excel(file_name, sheet_name=0, header=None)
wt_means, wt_lower, wt_upper = pile_up(wt_df)

rec8_2_df = pd.read_excel(file_name, sheet_name=1, header=None)
rec8_2_means, rec8_2_lower, rec8_2_upper = pile_up(rec8_2_df)

rec8_df = pd.read_excel(file_name, sheet_name=2, header=None)
rec8_means, rec8_lower, rec8_upper = pile_up(rec8_df)


x = [(i-250)/10 for i in range(len(wt_means))]

selected_x = select_region(x, x, 3)
selected_wt_means = select_region(x, wt_means, 3)
selected_wt_lower = select_region(x, wt_lower, 3)
selected_wt_upper = select_region(x, wt_upper, 3)

selected_rec8_2_means = select_region(x, rec8_2_means, 3)
selected_rec8_2_lower = select_region(x, rec8_2_lower, 3)
selected_rec8_2_upper = select_region(x, rec8_2_upper, 3)

selected_rec8_means = select_region(x, rec8_means, 3)
selected_rec8_lower = select_region(x, rec8_lower, 3)
selected_rec8_upper = select_region(x, rec8_upper, 3)

plt.plot(selected_x, selected_wt_means, color='#1b9e77', label='wild type')
plt.fill_between(selected_x, selected_wt_lower, selected_wt_upper, color='#1b9e77', alpha=.1)

plt.plot(selected_x, selected_rec8_means, color='#d95f02', label=r'$rec8-14D$')
plt.fill_between(selected_x, selected_rec8_lower, selected_rec8_upper, color='#d95f02', alpha=.1)

plt.plot(selected_x, selected_rec8_2_means, color='#7570b3', label=r'$rec8-14D$ repeat2')
plt.fill_between(selected_x, selected_rec8_2_lower, selected_rec8_2_upper, color='#7570b3', alpha=.1)

plt.xlabel('Distance from pericentromere border (kb)')
plt.ylabel('Mean calibrated reads')
plt.title('Pericentromere borders')
plt.legend()
plt.show()
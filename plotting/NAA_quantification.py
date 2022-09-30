import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


file_name = '/Users/kikawaryoku/Desktop/NAA_trail_1_quantification/test.xlsx'
df = pd.read_excel(file_name, engine='openpyxl', sheet_name=0)


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, h

wt_naa_means = []
wt_naa_cis = []
wt_no_naa_means = []
wt_no_naa_cis = []
bub1_aid_naa_means = []
bub1_aid_naa_cis = []
bub1_aid_no_naa_means = []
bub1_aid_no_naa_cis = []

time_range = range(0, 70, 10)


sub_df = df[(df['strain'] == 'wt') & (df['naa'] == '+')]
for i in time_range:
    mean, ci = mean_confidence_interval(sub_df[sub_df['time'] == i]['GFP_int'])
    wt_naa_means.append(mean)
    wt_naa_cis.append(ci)

sub_df = df[(df['strain'] == 'wt') & (df['naa'] == '-')]
for i in time_range:
    mean, ci = mean_confidence_interval(sub_df[sub_df['time'] == i]['GFP_int'])
    wt_no_naa_means.append(mean)
    wt_no_naa_cis.append(ci)

sub_df = df[(df['strain'] == 'Bub1-aid') & (df['naa'] == '+')]
for i in time_range:
    mean, ci = mean_confidence_interval(sub_df[sub_df['time'] == i]['GFP_int'])
    bub1_aid_naa_means.append(mean)
    bub1_aid_naa_cis.append(ci)

sub_df = df[(df['strain'] == 'Bub1-aid') & (df['naa'] == '-')]
for i in time_range:
    mean, ci = mean_confidence_interval(sub_df[sub_df['time'] == i]['GFP_int'])
    bub1_aid_no_naa_means.append(mean)
    bub1_aid_no_naa_cis.append(ci)


wt_naa_means = np.array(wt_naa_means)
wt_naa_cis = np.array(wt_naa_cis)
wt_no_naa_means = np.array(wt_no_naa_means)
wt_no_naa_cis = np.array(wt_no_naa_cis)
bub1_aid_naa_means = np.array(bub1_aid_naa_means)
bub1_aid_naa_cis = np.array(bub1_aid_naa_cis)
bub1_aid_no_naa_means = np.array(bub1_aid_no_naa_means)
bub1_aid_no_naa_cis = np.array(bub1_aid_no_naa_cis)

# plt.plot(time_range, wt_naa_means, label='wt + NAA')
# plt.fill_between(time_range, (wt_naa_means - wt_naa_cis), (wt_naa_means + wt_naa_cis), color='blue', alpha=0.1)
# plt.plot(time_range, wt_no_naa_means, label='wt - NAA')
# plt.fill_between(time_range, (wt_no_naa_means - wt_no_naa_cis), (wt_no_naa_means + wt_no_naa_cis), color='orange', alpha=0.1)
plt.plot(time_range, bub1_aid_naa_means, label='Bub1-aid + NAA')
# plt.fill_between(time_range, (bub1_aid_naa_means - bub1_aid_naa_cis), (bub1_aid_naa_means + bub1_aid_naa_cis), color='green', alpha=0.1)
plt.plot(time_range, bub1_aid_no_naa_means, label='Bub1-aid - NAA')
# plt.fill_between(time_range, (bub1_aid_no_naa_means - bub1_aid_no_naa_cis), (bub1_aid_no_naa_means + bub1_aid_no_naa_cis), color='red', alpha=0.1)
plt.xlabel('time (min)')
plt.ylabel('peri-CEN Sgo1-EGFP intensity')
plt.legend()
plt.show()

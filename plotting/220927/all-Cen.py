import pandas as pd
from pyBedGraph import BedGraph


flank = 25000
cen_file_name = 'centromere.xlsx'
cen = pd.read_excel(cen_file_name, sheet_name=0, header=None)
cen_starts = cen[3].tolist()
cen_ends = cen[4].tolist()
cen_mids = [int((cen_ends[i] -cen_starts[i]) / 2 + cen_starts[i]) for i in range(len(cen_starts))]
start_lists = [cen_mids[i] - flank for i in range(len(cen_starts))]
end_lists = [cen_mids[i] + flank for i in range(len(cen_starts))]

chromosome_sizes_file_name = 'myChrom.sizes'
data_file_name = 'tension.bedgraph'
bedGraph = BedGraph(chromosome_sizes_file_name, data_file_name)
chromo_names = ['chrI', 'chrII', 'chrIII', 'chrIV', 'chrV', 'chrVI', 'chrVII', 'chrVIII', 'chrIX', 'chrX', 'chrXI', 'chrXII', 'chrXIII', 'chrXIV', 'chrXV', 'chrXVI']
sums = []

for i in range(0, 16):
    bedGraph.load_chrom_data(chromo_names[i])
    bedGraph.load_chrom_bins(chromo_names[i], 100)
    test_intervals = [[chromo_names[i], start_lists[i], end_lists[i]]]
    sum = bedGraph.stats('sum', intervals=test_intervals)
    sums.append(sum[0])
    print(sum[0])

# dictionary of lists
dict = {'sum': sums}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('tension_cen_sums.csv')
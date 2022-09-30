from pyBedGraph import BedGraph
import pandas as pd

chromosome_sizes_file_name = 'myChrom.sizes'
data_file_name = 'no-tension.bedgraph'
bedGraph = BedGraph(chromosome_sizes_file_name, data_file_name)
chromo_names = ['chrI', 'chrII', 'chrIII', 'chrIV', 'chrV', 'chrVI', 'chrVII', 'chrVIII', 'chrIX', 'chrX', 'chrXI', 'chrXII', 'chrXIII', 'chrXIV', 'chrXV', 'chrXVI']
ends = [230218, 813184, 316620, 1531933, 576874, 270161, 1090940, 562643, 439888, 745751, 666816, 1078177, 924431, 784333, 1091291, 948066]
sums = []

for i in range(0, 16):
    bedGraph.load_chrom_data(chromo_names[i])
    bedGraph.load_chrom_bins(chromo_names[i], 100)
    test_intervals = [[chromo_names[i], 0, ends[i]]]
    sum = bedGraph.stats('sum', intervals=test_intervals)
    sums.append(sum[0])
    print(sum[0])

# dictionary of lists
dict = {'sum': sums}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('no-tension_bg_sums.csv')
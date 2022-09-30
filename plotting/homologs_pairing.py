import random
from itertools import zip_longest
import matplotlib.pyplot as plt
from tqdm import tqdm
import seaborn as sns
sns.set(style="whitegrid")


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def homologs_pairing():
    chromosomes = [x for x in range(3)] * 2
    counter = 0
    while len(chromosomes) > 0:
        paired_chromosomes = []
        random.shuffle(chromosomes)
        for first_chromosome, second_chromosome in grouper(chromosomes, 2):
            if first_chromosome == second_chromosome:
                paired_chromosomes.append(first_chromosome)
                paired_chromosomes.append(second_chromosome)
        for i in paired_chromosomes:
            chromosomes.remove(i)
        counter += 1
    return counter

y =[]
for j in tqdm(range(1000)):
    pairing_rounds = homologs_pairing()
    y.append(pairing_rounds)
mean = round(sum(y) / len(y), 1)
ax = sns.distplot(y)
plt.title('Distribution of simulations (mean={})'.format(mean))
plt.ylabel('density')
plt.xlabel('pairing rounds')
plt.show()

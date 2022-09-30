import random
import matplotlib.pyplot as plt
res = []
for i in range(10000):
    x_1 = random.randint(-4, 4)
    x_2 = random.randint(-4, 4)
    delta = abs(x_1 - x_2)
    res.append(delta)
plt.hist(res, bins=9, density=True)
plt.show()
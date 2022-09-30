import matplotlib.pyplot as plt
import numpy as np
arr = [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
arr = np.array(arr)
density = arr.sum() / len(arr)
upper_ept_arr = np.array([0] * 30)
lower_ept_arr = upper_ept_arr
img = np.array([upper_ept_arr, arr, lower_ept_arr])
print(density)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
import numpy as np
import matplotlib.pyplot as plt


data = np.zeros((10, 10))

print(np.size(data[:, 0]))

data[1:7, 3] = 1

data[[2, 6], 5:7] = 1

print(data)

plt.imshow(data.T, origin='lower')
plt.colorbar()
plt.savefig('array-slicing.png')
plt.show()

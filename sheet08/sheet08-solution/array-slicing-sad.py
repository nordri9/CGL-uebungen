import numpy as np
import matplotlib.pyplot as plt


data = np.zeros((10, 10))

data[2:7, 3] = 1
for i in (1, 7):
    data[i, 2] = 1


for i in (2, 6):
    data[i, 5:7] = 1

print(data)

plt.imshow(data.T, origin='lower')
plt.colorbar()
plt.savefig('array-slicing-sad.png')
plt.show()

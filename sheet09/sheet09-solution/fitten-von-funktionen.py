import numpy as np

import matplotlib.pyplot as plt

import scipy as sc

data = np.loadtxt("data.txt", dtype=float, delimiter=",")


x = data[:, 0]
y = data[:, 1]


def test(x, a, b):
    return a*np.sin(x*b)


param, param_cov = sc.optimize.curve_fit(test, x, y)

print(param)

y_fit = param[0]*np.sin(x*param[1])

plt.plot(x, y, 'o', color='red', label="data")
plt.plot(x, y_fit, '-', color='blue', label="data")

plt.savefig("fvf.pdf", format="pdf")
# plt.savefig('fvf.svg')
plt.show()

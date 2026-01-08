import numpy as np
import matplotlib.pyplot as plt

# Part 1
v = [1, 1]
M = np.matrix('1 1; 1 0')

ratios = []


results = []

for i in range(50):
    v.append(v[i+1]+v[i])

    vec = np.array([[v[i+1]],    # 2×1 column vector
                    [v[i]]])
    some_result = M @ vec        # or M.dot(vec)
    results.append(some_result)

    ratios.append(v[i]/v[i-1])

# print(v)
# print(ratios)
# print(results)
plt.plot(ratios, linestyle="none", marker="o")
plt.savefig("fibonacci.pdf")
plt.show()

# Part 2
# eigenwerte, eigenvektoren = np.linalg.eig(matrix)

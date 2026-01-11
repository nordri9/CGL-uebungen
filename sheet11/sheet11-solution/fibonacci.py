import numpy as np
import matplotlib.pyplot as plt

# Part 1
v = np.array([[1],
              [1]])

M = np.array([[1, 1],
              [1, 0]])

ratios = []

N = 50

for i in range(N):
    v = M @ v

    a_n = v[0, 0]
    a_nm1 = v[1, 0]
    ratios.append(a_n / a_nm1)


plt.plot(ratios, linestyle="none", marker="o")
plt.xlabel('n')
plt.ylabel(r'$a_n / a_{n-1}$')
plt.savefig("fibonacci.pdf")
plt.show()

# Part 2
eigenwerte, O = np.linalg.eig(M)
print("Eigenwerte:", eigenwerte)
print("Eigenvektoren (Spalten von vecs):")
print(O)

O_inv = np.linalg.inv(O)

lambda_1 = max(eigenwerte, key=abs)


def golden_approx(n):

    D_approx = np.array([[lambda_1**n, 0],
                         [0,           0]])

    Mn_approx = O @ D_approx @ O_inv

    v_n = Mn_approx @ v

    ratio = v_n[0, 0] / v_n[1, 0]
    print(ratio)


golden_approx(N)

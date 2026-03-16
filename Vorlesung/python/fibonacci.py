import numpy as np
import matplotlib.pyplot as plt

N =1000

v = np.array([[1],[1]])
M = np.array([[1,1],[1,0]])

ratios = []

for i in range(N):
    v = M @ v
    ratios.append(v[0]/v[1])
    
plt.plot(range(N),ratios)
plt.savefig("fibonacci.pdf")

eigenwerte, eigenvektoren = np.linalg.eig(M)

eigenvektoren_inv = np.linalg.inv(eigenvektoren)



def fib(n):
    D = np.array([[eigenwerte[0]**n,0],[0, eigenwerte[1]**n]])

    M = eigenvektoren_inv @ D @ eigenvektoren
    
print(fib(10))
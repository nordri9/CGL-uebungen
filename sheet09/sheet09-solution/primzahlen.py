import numpy as np

def sieb_des_eratosthenes(n):
    if n < 2:
        return []
    ist_prim = [True] * (n + 1)
    ist_prim[0] = ist_prim[1] = False

    for p in range(2, int(np.sqrt(n)) + 1):
        if ist_prim[p]:
            for i in range(p * p, n + 1, p):
                ist_prim[i] = False

    return [i for i, prim in enumerate(ist_prim) if prim]

n_limit = input("Enter a limit (N): ")
n_limit = int(n_limit)
print(f"Primzahlen bis {n_limit}: {sieb_des_eratosthenes(n_limit)}")
import numpy as np
np.random.seed(42)

data = np.random.rand(100)

print(data)


def quicksort(liste):
    if(len(liste)<=1):
        return liste
    else:
        pivot = 
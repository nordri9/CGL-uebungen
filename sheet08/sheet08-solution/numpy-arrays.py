import numpy as np
np.random.seed(42)
data = np.random.rand(100, 2)

print(np.size(data))
print(data[0,1])
print(data[-1,:])
#print(data[:,10]) #gibt eine Fehlermeldung aus, da wir nur 2 Spalten haben 
print(data[50:59])
print(data[:,0])
print(np.mean(data[50:99,0]))
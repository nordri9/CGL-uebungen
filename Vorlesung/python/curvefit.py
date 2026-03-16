import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt("data.txt",dtype=float,delimiter=",")

t = data[:,0]
y = data[:,1]

f = lambda t ,A ,d ,o: A*np.exp(-d*t)*np.sin(o*t)
p0=(y[0],1,1)
popt, pcov = curve_fit(f,t,y,p0) # popt => parameter optimal | pcov => parameter covariance
print(popt)

perr = np.sqrt(np.diag(pcov))  # Unsicherheit jedes Parameters
print(perr)

plt.scatter(t,y, label="data")
plt.plot(t,f(t, *popt), label="fit")
plt.legend()
plt.savefig("fit.pdf")
plt.show()
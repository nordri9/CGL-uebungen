import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

data = np.loadtxt("data.txt", dtype=float, delimiter=",")
x = data[:, 0]
y = data[:, 1]

def damped_sine(x, a, d, b):
    return a * np.exp(-d * x) * np.sin(b * x)

param, param_cov = opt.curve_fit(damped_sine, x, y)


print(f"Fit Results: Amp={param[0]:.3f}, Damping={param[1]:.3f}, Freq={param[2]:.3f}")

y_fit = damped_sine(x, *param)

plt.plot(x, y, 'o', color='red', label="data")
plt.plot(x, y_fit, '-', color='blue', label="fit")

plt.title("Damped Oscillation")
plt.legend()
plt.savefig("fitten-von-funktionen.pdf")
plt.show()
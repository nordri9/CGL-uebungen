import numpy as np
import matplotlib.pyplot as plt


# Funktion zur Berechnung der gedämpften harmonischen Schwingung
def damped_oscillation(t, A, gamma, omega):
    """
    Berechnet die Auslenkung einer gedämpften harmonischen Schwingung zur Zeit t.

    x(t) = A * e^(-gamma * t) * cos(omega * t)
    """
    return A * np.exp(-gamma * t) * np.cos(omega * t)


time_steps = np.linspace(0, 10, num=500)

plt.scatter(time_steps, damped_oscillation(time_steps, 1, .2, 2*np.pi))
plt.xlabel("Zeit t")
plt.title("damped oscillator")
plt.ylabel("Auslenkung x(t)")
plt.legend(['damped oscillation'])
plt.savefig('damped_oscillation.svg')
plt.show()

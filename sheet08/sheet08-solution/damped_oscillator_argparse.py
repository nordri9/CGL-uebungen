import numpy as np
import matplotlib.pyplot as plt
import argparse


# Funktion zur Berechnung der gedämpften harmonischen Schwingung
def damped_oscillation(t, A, gamma, omega):
    """
    Berechnet die Auslenkung einer gedämpften harmonischen Schwingung zur Zeit t.

    x(t) = A * e^(-gamma * t) * cos(omega * t)
    """
    return A * np.exp(-gamma * t) * np.cos(omega * t)


time_steps = np.linspace(0, 10, num=500)

parser = argparse.ArgumentParser()
parser.add_argument("-A", "--amplitude", "-amplitude", type=float, default=1.0,
                    help="The initial amplitude.")

parser.add_argument("-g", "--gamma", "-gamma", type=float, default=0.0,
                    help="The damping coefficient.")

parser.add_argument("-o", "--omega", "-omega", type=float, required=True,
                    help="The natural frequency.")
args = parser.parse_args()


plt.scatter(time_steps, damped_oscillation(
    time_steps, args.amplitude, args.gamma, args.omega))
plt.xlabel("Zeit t")
plt.ylabel("Auslenkung x(t)")
plt.legend(['damped oscillation'])
plt.savefig('damped_oscillator_argparse.png')
plt.show()

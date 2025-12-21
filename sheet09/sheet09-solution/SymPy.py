import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t', real=True)
A = sp.symbols('A')
lam = sp.symbols('lambda', positive=True, real=True)
omega = sp.symbols('omega', positive=True, real=True)

f = A * sp.exp(-lam * t) * sp.cos(omega * t)

f_prime = sp.diff(f, t)

f_integral = sp.integrate(f, t)

f_limit = sp.limit(f, t, sp.oo)

f_func_np = sp.lambdify((t, A, lam, omega), f, 'numpy')
df_func_np = sp.lambdify((t, A, lam, omega), f_prime, 'numpy')

A_val = 2
lam_val = 0.5
omega_val = 3

t_vals = np.linspace(0, 10, 1000)

y_f = f_func_np(t_vals, A_val, lam_val, omega_val)
y_df = df_func_np(t_vals, A_val, lam_val, omega_val)

plt.plot(t_vals, y_f, label="Schwingung", color='blue')
plt.plot(t_vals, y_df, label="Ableitung", color='red')

plt.title("Gedämpfte Schwingung und 1. Ableitung")
plt.xlabel("Zeit (t)")
plt.ylabel("Amplitude")
plt.legend()
plt.savefig("SymPy.pdf")
plt.show()


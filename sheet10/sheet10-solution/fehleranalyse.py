import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Teil A: Symbolische Berechnung (sympy)

t = sp.symbols('t', real=True)
A = sp.symbols('A')
lam = sp.symbols('lambda', positive=True, real=True)
omega = sp.symbols('omega', positive=True, real=True)
delt_A = sp.symbols('delt_A', real=True)
delt_lam = sp.symbols('delt_lam', real=True)
delt_omega = sp.symbols('delt_omega', real=True)

x = A * sp.exp(-lam * t) * sp.cos(omega * t)

x_diff_A = sp.diff(x, A)
x_diff_lam = sp.diff(x, lam)
x_diff_omega = sp.diff(x, omega)

delt_x = delt_A * sp.Abs(x_diff_A) + delt_lam * \
    sp.Abs(x_diff_lam) + delt_omega * sp.Abs(x_diff_omega)

x_np = sp.lambdify((t, A, lam, omega), x, 'numpy')
delt_x_np = sp.lambdify((t, A, lam, omega, delt_A, delt_lam,
                         delt_omega), delt_x, 'numpy')

# Teil B: Numerische Simulation & Plot(matplotlib)

t_vals = np.linspace(0, 20, 400)

# Fall 1: A-Unsicherheit

A_val, dA_val = 10.0, 1.0
gamma_val, dgamma_val = 0.1, 0.0
omega_val, domega_val = 2.0, 0.0

x_vals = x_np(t_vals, A_val, gamma_val, omega_val)
dx_vals = delt_x_np(t_vals, A_val, gamma_val, omega_val,
                    dA_val, dgamma_val, domega_val)

plt.figure()
plt.plot(t_vals, x_vals, label='x(t)')
plt.fill_between(t_vals,
                 x_vals - dx_vals,
                 x_vals + dx_vals,
                 alpha=0.3, label='Unsicherheit A')

plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Gedämpfte Schwingung mit Unsicherheit in A')
plt.legend()
plt.axhline(0, color='black')
plt.savefig("fehleranalyse-1.pdf")
plt.show()


# Fall 2: omega-Unsicherheit

A_val2, dA_val2 = 10.0, 0.0
gamma_val2, dgamma_val2 = 0.1, 0.0
omega_val2, domega_val2 = 2.0, 0.2

x_vals2 = x_np(t_vals, A_val2, gamma_val2, omega_val2)
dx_vals2 = delt_x_np(t_vals, A_val2, gamma_val2, omega_val2,
                     dA_val2, dgamma_val2, domega_val2)


plt.figure()
plt.plot(t_vals, x_vals2, label='x(t)', color='C1')
plt.fill_between(t_vals,
                 x_vals2 - dx_vals2,
                 x_vals2 + dx_vals2,
                 color='C1', alpha=0.3, label='Unsicherheit omega')

plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Gedaempfte Schwingung mit Unsicherheit in omega')
plt.legend()
plt.axhline(0, color='black')
plt.savefig("fehleranalyse-2.pdf")
plt.show()

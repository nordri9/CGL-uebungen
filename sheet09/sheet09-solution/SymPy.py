import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


t = sp.symbols('t', real=True)
A = sp.symbols('A')
lam = sp.symbols('lambda', positive=True, real=True)
omega = sp.symbols('omega', positive=True, real=True)

f = A*sp.exp(-lam*t)*sp.cos(omega*t)

f_prime = sp.diff(f,t)

f_integral = sp.integrate(f,t)

f_limit = sp.limit(f,t,sp.oo)
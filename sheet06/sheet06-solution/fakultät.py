import math


def fak(n):
    assert isinstance(n, int) and n >= 0, (
        "Die gegebene Zahl ist keine natürliche Zahl (>= 0)."
    )

    if n == 0:
        return 1

    result = 1
    for k in range(1, n + 1):
        result *= k

    return result


assert fak(0) == 1
assert fak(1) == 1
assert fak(3) == 6
assert fak(4) == 24


def berechne_e(n_terme):
    e_approx = 0.0
    for k in range(n_terme):
        term = 1.0 / fak(k)
        e_approx += term

    return e_approx


# Genauigkeit der Approximation
N = 15
naeherung_e = berechne_e(N)

print(f"\nNäherung mit {N} Termen:")
print(f"e = {naeherung_e}")
print(f"Python's math.e = {math.e}")

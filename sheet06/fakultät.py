def fak(n):

    assert isinstance(n, int) and n >= 0, "Die gegebene Zahl ist keine natürliche Zahl (>= 0)."
    
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
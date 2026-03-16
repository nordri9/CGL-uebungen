def fak(n):
    assert isinstance(n,int) and n>=0, "Zahl ist nicht natürlcht oder null"
    prod=1
    if n == 0:
        return 1
    for i in range(1,n+1):
        prod *= i
#        print(i,":",prod)
    return prod

assert fak(0) == 1
assert fak(10) == 3628800

def euler(n):
    e = 1
    for i in range(1,n+1):
        e += 1/fak(i)
        print(i,":",e)
    return e

print(euler(10))

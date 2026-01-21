# import numpy as np

y = 1

for i in range(1, 10):
    y = y * i
    print(y)

print("hallo")

for e in range(1, 30):
    if e % 7 == 0:
        print(e, "divisible by 7")

l = ["rot", "grün", "blau"]

l = l+["orange"]

print(type(l))

for i in l:
    print(i)

l_2 = [1,2,3]
m = l_2
n = l_2.copy()
m = l_2 + [4]


print(n)
print(m)

d = dict(Montag="Monday", Dienstag="Tuesday", Mittwoch="Wednesday")

k = input("Ihr Text: ")

if k in d.keys():
    print(d[k])

else:
    print("nix")


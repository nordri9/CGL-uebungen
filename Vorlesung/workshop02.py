from contextlib import nullcontext
from numpy import subtract


def summieren(*zahlen):
    ergebnis = 0
    for x in zahlen:
        ergebnis += x
    return print(ergebnis)


summieren(1, 2, 3, 4)


def f(**kwargs):
    for x, y in kwargs.items():
        print(f"{x}:{y}")


f(farbe="rot", zahl=42)

l = {1, 2, 5, 6, 4, 5}


def abstand_von_5(x):
    return abs(5 - x)


assert abstand_von_5(3) == 2

assert abstand_von_5(6) == 1

print(sorted(l, key=abstand_von_5))


print(sorted(l,key= lambda x: abs(x - 5)))

try:
    file = open("xy.dat", "r")

except Exception as e:
    print("Fehler beim Öffnen:",e)
    exit()

lines = file.readlines()
type(lines)
for i, line in enumerate(lines):
    if line.strip() == '':
        pass
    else:
        s = line.strip() # Zeilenende-Zeichen entfernen
        print("Zeile",i,"ist",s)

l = "hallo welt".split()
try:
    for i in l:
        l_f = float(l[i])
        print(l_f[i])
        
except Exception as e:
    print("Fail:",e)
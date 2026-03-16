N = 1000000000
a = []
b = []
for i in range(2,N):
    a.append(i)    

#print(a)
p_zahlen = []

while len(a)>0:
    n = a[0]
    for i in a:
        if i == n:
            b.append(i)
        if i%n ==0:
            a.remove(i)
            
            
print(b)

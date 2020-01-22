a = int(input())
b = input().split()
L = []

for i in range(0, 23) :
    L.append(0)

for j in range(0, a) :
    L[int(b[j]) -1] += 1

for k in range(0, 23) :
    print(L[k], end = " ")

a = int(input())

L = []
for i in range(0, a) :
    b = input().split()
    L.append(b)

M = []
for i in range(0, 19) :
    M.append([])
    for j in range(0, 19) :
        M[i].append(0)

for i in range(0, a) :
    M[int(L[i][0]) -1][int(L[i][1]) -1] = 1
    
for i in range(0, 19) :
    for j in range(0, 19) :
        print(M[i][j], end = " ")
    print()

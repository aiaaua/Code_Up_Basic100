a = int(input())
b = input().split()
min = 23

for i in range(0, a) :
    if (int(b[i]) < min) :
        min = int(b[i])
print(min)

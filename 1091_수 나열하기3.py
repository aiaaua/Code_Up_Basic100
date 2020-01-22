a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
n = int(d)
result = a

for i in range(1, n) :
    result = result*b + c
print(result)

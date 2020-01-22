a, b, c = input().split()
a = int(a)
r = int(b)
n = int(c)
product = a

for i in range(1, n) :
    product = product*r
print(product)

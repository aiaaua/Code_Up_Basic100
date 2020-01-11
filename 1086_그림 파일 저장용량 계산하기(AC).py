a, b, c =  input().split()

w = int(a)
h = int(b)
b = int(c)

size = "%.2f" % ((w*h*b)/(8*1024*1024))

print(size, "MB")

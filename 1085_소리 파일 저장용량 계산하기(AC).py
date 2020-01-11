a, b, c, d = input().split()
hz = int(a)
bit = int(b)
ch = int(c)
sec = int(d)

size = "%.1f" % ((hz*bit*ch*sec)/(8*1024*1024))
print(size, "MB")

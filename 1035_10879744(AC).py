a = input()
b = '0x' + a
c = oct(int(b, 16))
print(c[2:])

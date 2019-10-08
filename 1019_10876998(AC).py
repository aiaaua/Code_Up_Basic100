a, b, c = input().split('.')
a = str(a)
b = str(b)
c = str(c)
d = str(0)
if (len(a) == 2) : 
    a = d+d+a
if (len(b) == 1) : 
    b = d+b
if (len(c) == 1) : 
    c = d+c
    
print(a + "." + b + "." + c)

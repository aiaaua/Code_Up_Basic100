a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(int((a==True and b==True) or (a==False and b==False)))

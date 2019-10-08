a = input()
i = 0

while (i<len(a)) : 
    b = int(a[i:(i+1)])
    c = str(b*(10**(4-i)))
    print("[" + c + "]")
    i += 1

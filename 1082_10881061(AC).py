a = input()
a = '0x' + a

for i in range(1,16) :
    temp = int(a, 16)
    result = hex(temp*i).upper()
    i_ = hex(i).upper()
    print (a[2:]+"*"+i_[2:]+"="+result[2:])

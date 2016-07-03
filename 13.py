a=256
print bin(a)
num=0
for i in bin(a):
    if i=='1':
        num = num + 1
print num
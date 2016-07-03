a = 'cagy'
b = 3
m = list(a)
for i in range(len(m)):
    m[i] = chr(ord(m[i]) + b)
    if m[i] > 'z':
        m[i] = chr(ord(m[i]) - 26)
print ''.join(m)
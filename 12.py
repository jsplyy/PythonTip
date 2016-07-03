L=[2,8,3,50]
totoal = 1
for i in L:
    totoal = totoal * i
    if totoal%10==0:
        totoal = totoal/10
if totoal%10==0:
    totoal = totoal/10
if totoal%2==0:
    print '0'
else:
    print '1'